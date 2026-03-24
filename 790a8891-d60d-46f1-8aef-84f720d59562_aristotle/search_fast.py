"""Efficient graph search using vectorized numpy operations."""
import numpy as np
import random
import sys

def search_graph(n, seed=42, max_restarts=200, max_steps=1000000):
    N = 4*n - 2
    rng = random.Random(seed + n)
    target_deg = 2*n - 2
    
    for restart in range(max_restarts):
        adj = np.zeros((N, N), dtype=np.int8)
        deg = np.zeros(N, dtype=np.int32)
        
        edges = [(i,j) for i in range(N) for j in range(i+1,N)]
        rng.shuffle(edges)
        for i,j in edges:
            if deg[i] < target_deg and deg[j] < target_deg:
                adj[i,j] = adj[j,i] = 1
                deg[i] += 1
                deg[j] += 1
        
        # Codegree matrix
        cd = (adj @ adj).astype(np.int32)
        
        def full_violation():
            v = 0
            for i in range(N):
                for j in range(i+1, N):
                    c = int(cd[i,j])
                    if adj[i,j]:
                        if c > n-2: v += c - (n-2)
                    else:
                        comp = N - 2 - int(deg[i]) - int(deg[j]) + c
                        if comp > n-1: v += comp - (n-1)
            return v
        
        viol = full_violation()
        if viol == 0:
            return adj, restart
        
        for step in range(max_steps):
            i = rng.randint(0, N-1)
            j = rng.randint(0, N-1)
            if i == j: continue
            if i > j: i, j = j, i
            
            was_edge = int(adj[i,j])
            sign = -1 if was_edge else 1
            
            new_deg_i = int(deg[i]) + sign
            new_deg_j = int(deg[j]) + sign
            
            # Vectorized computation of violation delta
            old_v = 0
            new_v = 0
            
            # Pair (i,j) itself
            c_ij = int(cd[i,j])
            if was_edge:
                if c_ij > n-2: old_v += c_ij - (n-2)
                comp = N - 2 - new_deg_i - new_deg_j + c_ij
                if comp > n-1: new_v += comp - (n-1)
            else:
                comp = N - 2 - int(deg[i]) - int(deg[j]) + c_ij
                if comp > n-1: old_v += comp - (n-1)
                if c_ij > n-2: new_v += c_ij - (n-2)
            
            # Get adjacency rows
            adj_j_arr = adj[j]  # numpy array
            adj_i_arr = adj[i]  # numpy array
            
            # For pairs (i,k), k != i,j:
            # old cd[i,k], new cd[i,k] = old + sign * adj[j,k]
            cd_i = cd[i].copy()  # codegrees of i with all
            delta_cd_i = sign * adj_j_arr  # change in cd[i,k]
            new_cd_i = cd_i + delta_cd_i
            
            # For pairs (j,k), k != i,j:
            cd_j = cd[j].copy()
            delta_cd_j = sign * adj_i_arr
            new_cd_j = cd_j + delta_cd_j
            
            deg_arr = deg.copy()
            
            # Process pairs (i,k) for k != i,j
            for k in range(N):
                if k == i or k == j: continue
                
                c_old = int(cd_i[k])
                c_new = int(new_cd_i[k])
                dk = int(deg_arr[k])
                
                if adj[i,k]:
                    if c_old > n-2: old_v += c_old - (n-2)
                    if c_new > n-2: new_v += c_new - (n-2)
                else:
                    oc = N - 2 - int(deg[i]) - dk + c_old
                    nc = N - 2 - new_deg_i - dk + c_new
                    if oc > n-1: old_v += oc - (n-1)
                    if nc > n-1: new_v += nc - (n-1)
                
                c_old = int(cd_j[k])
                c_new = int(new_cd_j[k])
                
                if adj[j,k]:
                    if c_old > n-2: old_v += c_old - (n-2)
                    if c_new > n-2: new_v += c_new - (n-2)
                else:
                    oc = N - 2 - int(deg[j]) - dk + c_old
                    nc = N - 2 - new_deg_j - dk + c_new
                    if oc > n-1: old_v += oc - (n-1)
                    if nc > n-1: new_v += nc - (n-1)
            
            delta = new_v - old_v
            
            if delta <= 0 or rng.random() < 0.003:
                adj[i,j] = 1 - was_edge
                adj[j,i] = 1 - was_edge
                deg[i] = new_deg_i
                deg[j] = new_deg_j
                
                # Update cd matrix
                for k in range(N):
                    if k != i:
                        cd[i,k] += sign * int(adj_j_arr[k])
                        cd[k,i] += sign * int(adj_j_arr[k])
                    if k != j:
                        cd[j,k] += sign * int(adj_i_arr[k])
                        cd[k,j] += sign * int(adj_i_arr[k])
                
                viol += delta
                if viol == 0:
                    return adj, restart
        
        if restart % 5 == 0:
            print(f"  n={n} restart {restart}: viol={viol}", flush=True)
    
    return None, -1


def verify(adj, n):
    N = adj.shape[0]
    deg = adj.sum(axis=1)
    cd = adj @ adj
    for i in range(N):
        for j in range(i+1, N):
            c = int(cd[i,j])
            if adj[i,j]:
                if c > n-2: return False, f"edge ({i},{j}) cd={c}"
            else:
                comp = N - 2 - int(deg[i]) - int(deg[j]) + c
                if comp > n-1: return False, f"non-edge ({i},{j}) comp_cd={comp}"
    return True, "OK"


def adj_to_string(adj, N):
    result = []
    for j in range(N):
        for i in range(j):
            result.append("1" if adj[i,j] else "0")
    return "".join(result)


if __name__ == "__main__":
    for n in range(2, 21):
        N = 4*n - 2
        print(f"n={n} (N={N}):", flush=True)
        adj, restart = search_graph(n, max_restarts=30, max_steps=200000)
        if adj is not None:
            ok, msg = verify(adj, n)
            print(f"  Found at restart {restart}, verified={ok}")
        else:
            print(f"  FAILED")
