"""Fully vectorized graph search."""
import numpy as np
import random

def search_graph(n, seed=42, max_restarts=300, max_steps=2000000):
    N = 4*n - 2
    rng = random.Random(seed + n)
    np_rng = np.random.RandomState(seed + n)
    target_deg = 2*n - 2
    
    for restart in range(max_restarts):
        adj = np.zeros((N, N), dtype=np.int32)
        deg = np.zeros(N, dtype=np.int32)
        
        edges = [(i,j) for i in range(N) for j in range(i+1,N)]
        rng.shuffle(edges)
        for i,j in edges:
            if deg[i] < target_deg and deg[j] < target_deg:
                adj[i,j] = adj[j,i] = 1
                deg[i] += 1
                deg[j] += 1
        
        cd = adj @ adj  # codegree matrix
        
        # Compute violation using vectorized ops
        def full_violation_vec():
            upper = np.triu_indices(N, 1)
            c = cd[upper]
            is_edge = adj[upper]
            d_i = deg[upper[0]]
            d_j = deg[upper[1]]
            
            edge_viol = np.maximum(c - (n-2), 0) * is_edge
            comp_cd = N - 2 - d_i - d_j + c
            nonedge_viol = np.maximum(comp_cd - (n-1), 0) * (1 - is_edge)
            return int(np.sum(edge_viol) + np.sum(nonedge_viol))
        
        viol = full_violation_vec()
        if viol == 0:
            return adj, restart
        
        # Precompute indices for fast access
        # For each pair, compute contribution to violation
        
        for step in range(max_steps):
            i = rng.randint(0, N-1)
            j = rng.randint(0, N-1)
            if i == j: continue
            if i > j: i, j = j, i
            
            was_edge = adj[i,j]
            sign = 1 - 2*was_edge  # +1 if adding, -1 if removing
            
            new_deg_i = deg[i] + sign
            new_deg_j = deg[j] + sign
            
            # Compute delta violation using numpy
            # Affected pairs: (i,j), (i,k) for all k, (j,k) for all k
            
            # Create mask for valid k
            mask = np.ones(N, dtype=bool)
            mask[i] = mask[j] = False
            
            # --- Pair (i,j) ---
            c_ij = cd[i,j]
            old_v_ij = 0
            new_v_ij = 0
            if was_edge:
                old_v_ij = max(0, c_ij - (n-2))
                comp = N - 2 - new_deg_i - new_deg_j + c_ij
                new_v_ij = max(0, comp - (n-1))
            else:
                comp = N - 2 - deg[i] - deg[j] + c_ij
                old_v_ij = max(0, comp - (n-1))
                new_v_ij = max(0, c_ij - (n-2))
            
            # --- Pairs (i,k) for k != i,j ---
            cd_ik = cd[i, mask].copy()  # old codegrees
            new_cd_ik = cd_ik + sign * adj[j, mask]
            is_edge_ik = adj[i, mask]
            dk = deg[mask]
            
            old_edge_v = np.maximum(cd_ik - (n-2), 0) * is_edge_ik
            new_edge_v = np.maximum(new_cd_ik - (n-2), 0) * is_edge_ik
            
            old_comp = N - 2 - deg[i] - dk + cd_ik
            new_comp = N - 2 - new_deg_i - dk + new_cd_ik
            old_nonedge_v = np.maximum(old_comp - (n-1), 0) * (1 - is_edge_ik)
            new_nonedge_v = np.maximum(new_comp - (n-1), 0) * (1 - is_edge_ik)
            
            delta_ik = int(np.sum(new_edge_v - old_edge_v + new_nonedge_v - old_nonedge_v))
            
            # --- Pairs (j,k) for k != i,j ---
            cd_jk = cd[j, mask].copy()
            new_cd_jk = cd_jk + sign * adj[i, mask]
            is_edge_jk = adj[j, mask]
            
            old_edge_v = np.maximum(cd_jk - (n-2), 0) * is_edge_jk
            new_edge_v = np.maximum(new_cd_jk - (n-2), 0) * is_edge_jk
            
            old_comp = N - 2 - deg[j] - dk + cd_jk
            new_comp = N - 2 - new_deg_j - dk + new_cd_jk
            old_nonedge_v = np.maximum(old_comp - (n-1), 0) * (1 - is_edge_jk)
            new_nonedge_v = np.maximum(new_comp - (n-1), 0) * (1 - is_edge_jk)
            
            delta_jk = int(np.sum(new_edge_v - old_edge_v + new_nonedge_v - old_nonedge_v))
            
            delta = (new_v_ij - old_v_ij) + delta_ik + delta_jk
            
            if delta <= 0 or rng.random() < 0.002:
                # Apply flip
                old_adj_j = adj[j].copy()
                old_adj_i = adj[i].copy()
                
                adj[i,j] = 1 - was_edge
                adj[j,i] = 1 - was_edge
                deg[i] = new_deg_i
                deg[j] = new_deg_j
                
                # Update cd matrix: cd[i,:] += sign * adj[j,:], cd[:,i] same
                cd[i,:] += sign * old_adj_j
                cd[:,i] += sign * old_adj_j
                cd[j,:] += sign * old_adj_i
                cd[:,j] += sign * old_adj_i
                
                viol += delta
                if viol <= 0:
                    # Recompute to avoid floating point drift
                    viol = full_violation_vec()
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
                if c > n-2: return False
            else:
                comp = N - 2 - int(deg[i]) - int(deg[j]) + c
                if comp > n-1: return False
    return True


def adj_to_string(adj, N):
    result = []
    for j in range(N):
        for i in range(j):
            result.append("1" if adj[i,j] else "0")
    return "".join(result)


if __name__ == "__main__":
    for n in range(2, 31):
        N = 4*n - 2
        print(f"n={n} (N={N}):", flush=True)
        adj, restart = search_graph(n, max_restarts=50, max_steps=500000)
        if adj is not None:
            ok = verify(adj, n)
            print(f"  Found at restart {restart}, verified={ok}")
        else:
            print(f"  FAILED")
