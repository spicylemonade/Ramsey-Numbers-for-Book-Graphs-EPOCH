"""Efficient graph search using numpy."""
import numpy as np
import random

def search_graph(n, seed=42, max_restarts=100, max_steps=500000):
    N = 4*n - 2
    rng = random.Random(seed + n)
    target_deg = 2*n - 2
    
    for restart in range(max_restarts):
        # Random graph targeting degree target_deg
        adj = np.zeros((N, N), dtype=np.int8)
        deg = np.zeros(N, dtype=np.int32)
        
        edges = [(i,j) for i in range(N) for j in range(i+1,N)]
        rng.shuffle(edges)
        for i,j in edges:
            if deg[i] < target_deg and deg[j] < target_deg:
                adj[i,j] = adj[j,i] = 1
                deg[i] += 1
                deg[j] += 1
        
        # Precompute codegree matrix: cd[i,j] = number of common neighbors
        cd = adj @ adj  # cd[i,j] = sum_k adj[i,k]*adj[j,k]
        # Note: cd[i,i] = deg[i], cd[i,j] for i!=j is the codegree
        
        def compute_violation():
            v = 0
            for i in range(N):
                for j in range(i+1, N):
                    if adj[i,j]:
                        if cd[i,j] > n-2:
                            v += cd[i,j] - (n-2)
                    else:
                        comp_cd = N - 2 - deg[i] - deg[j] + cd[i,j]
                        if comp_cd > n-1:
                            v += comp_cd - (n-1)
            return v
        
        viol = int(compute_violation())
        if viol == 0:
            return adj, restart
        
        for step in range(max_steps):
            i = rng.randint(0, N-1)
            j = rng.randint(0, N-1)
            if i == j: continue
            if i > j: i, j = j, i
            
            was_edge = adj[i,j]
            sign = -1 if was_edge else 1
            
            # Compute violation change
            new_deg_i = deg[i] + sign
            new_deg_j = deg[j] + sign
            
            old_v = 0
            new_v = 0
            
            # Pair (i,j) itself
            c = int(cd[i,j])
            if was_edge:
                if c > n-2: old_v += c - (n-2)
                comp = N - 2 - new_deg_i - new_deg_j + c
                if comp > n-1: new_v += comp - (n-1)
            else:
                comp = N - 2 - deg[i] - deg[j] + c
                if comp > n-1: old_v += comp - (n-1)
                if c > n-2: new_v += c - (n-2)
            
            # Pairs involving i (except j)
            # When flipping (i,j): cd[i,k] changes by sign * adj[j,k] for all k
            # Also deg[i] changes by sign
            adj_j = adj[j]  # row j
            adj_i = adj[i]  # row i
            
            for k in range(N):
                if k == i or k == j: continue
                
                # Pair (i,k)
                c_ik = int(cd[i,k])
                new_c_ik = c_ik + sign * int(adj_j[k])
                e_ik = adj[i,k]
                
                if e_ik:
                    if c_ik > n-2: old_v += c_ik - (n-2)
                    if new_c_ik > n-2: new_v += new_c_ik - (n-2)
                else:
                    oc = N - 2 - int(deg[i]) - int(deg[k]) + c_ik
                    nc = N - 2 - new_deg_i - int(deg[k]) + new_c_ik
                    if oc > n-1: old_v += oc - (n-1)
                    if nc > n-1: new_v += nc - (n-1)
                
                # Pair (j,k)
                c_jk = int(cd[j,k])
                new_c_jk = c_jk + sign * int(adj_i[k])
                e_jk = adj[j,k]
                
                if e_jk:
                    if c_jk > n-2: old_v += c_jk - (n-2)
                    if new_c_jk > n-2: new_v += new_c_jk - (n-2)
                else:
                    oc = N - 2 - int(deg[j]) - int(deg[k]) + c_jk
                    nc = N - 2 - new_deg_j - int(deg[k]) + new_c_jk
                    if oc > n-1: old_v += oc - (n-1)
                    if nc > n-1: new_v += nc - (n-1)
            
            delta = new_v - old_v
            
            accept = (delta <= 0) or (rng.random() < 0.003)
            if accept:
                # Apply flip
                adj[i,j] = 1 - was_edge
                adj[j,i] = 1 - was_edge
                deg[i] = new_deg_i
                deg[j] = new_deg_j
                # Update codegree matrix
                # cd[i,k] += sign * adj[j,k] for all k != i
                # cd[k,i] += sign * adj[j,k] for all k != i  
                # cd[j,k] += sign * adj[i,k] for all k != j (use OLD adj[i])
                # But adj[i] has changed! Need to use the right adj[i]
                # adj[i,j] has changed but we need adj[i,k] for k != j
                # adj[i,k] for k != j hasn't changed yet... wait, only adj[i,j] changed
                # So adj_i[k] for k != j is still correct
                
                for k in range(N):
                    if k != i:
                        cd[i,k] += sign * int(adj_j[k])
                        cd[k,i] += sign * int(adj_j[k])
                    if k != j:
                        # Need original adj[i,k] (before flip)
                        # adj[i,j] changed but adj[i,k] for k!=j didn't
                        cd[j,k] += sign * int(adj_i[k])
                        cd[k,j] += sign * int(adj_i[k])
                
                viol += delta
                
                if viol == 0:
                    return adj, restart
        
        if restart % 10 == 0:
            print(f"  n={n} restart {restart}: viol={viol}")
    
    return None, -1


def verify(adj, n):
    N = adj.shape[0]
    deg = adj.sum(axis=1)
    cd = adj @ adj
    for i in range(N):
        for j in range(i+1, N):
            c = int(cd[i,j])
            if adj[i,j]:
                if c > n-2:
                    return False, f"edge ({i},{j}) cd={c}"
            else:
                comp = N - 2 - int(deg[i]) - int(deg[j]) + c
                if comp > n-1:
                    return False, f"non-edge ({i},{j}) comp_cd={comp}"
    return True, "OK"


def adj_to_string(adj, N):
    result = []
    for j in range(N):
        for i in range(j):
            result.append("1" if adj[i,j] else "0")
    return "".join(result)


if __name__ == "__main__":
    for n in range(2, 12):
        N = 4*n - 2
        print(f"n={n} (N={N}):", flush=True)
        adj, restart = search_graph(n, max_restarts=30, max_steps=200000)
        if adj is not None:
            ok, msg = verify(adj, n)
            print(f"  Found at restart {restart}, verified={ok} ({msg})")
        else:
            print(f"  FAILED")
