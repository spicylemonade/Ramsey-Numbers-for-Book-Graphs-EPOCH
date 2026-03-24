"""Optimized search for n=4 using incremental codegree updates."""
import random

def search_graph(n):
    N = 4 * n - 2
    rng = random.Random(42)
    
    for restart in range(200):
        # Start with random graph
        adj = [[False]*N for _ in range(N)]
        deg = [0]*N
        
        all_edges = [(i,j) for i in range(N) for j in range(i+1,N)]
        rng.shuffle(all_edges)
        target = 2*n - 2
        for i,j in all_edges:
            if deg[i] < target and deg[j] < target:
                adj[i][j] = adj[j][i] = True
                deg[i] += 1
                deg[j] += 1
        
        # Precompute codegrees for all pairs
        codeg = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(i+1, N):
                c = 0
                for k in range(N):
                    if k != i and k != j and adj[i][k] and adj[j][k]:
                        c += 1
                codeg[i][j] = codeg[j][i] = c
        
        def compute_violation():
            v = 0
            for i in range(N):
                for j in range(i+1, N):
                    if adj[i][j]:
                        if codeg[i][j] > n-2:
                            v += codeg[i][j] - (n-2)
                    else:
                        # complement codegree = N-2-deg[i]-deg[j]+codeg[i][j]
                        comp_cd = N - 2 - deg[i] - deg[j] + codeg[i][j]
                        if comp_cd > n-1:
                            v += comp_cd - (n-1)
            return v
        
        viol = compute_violation()
        
        if viol == 0:
            return adj, restart
        
        # Local search with incremental updates
        for step in range(200000):
            if viol == 0:
                return adj, restart
            
            i = rng.randint(0, N-1)
            j = rng.randint(0, N-1)
            if i == j:
                continue
            if i > j:
                i, j = j, i
            
            # Compute change in violation if we flip (i,j)
            was_edge = adj[i][j]
            
            # Delta codegrees for affected pairs
            # Flipping (i,j) affects codeg[i][k] and codeg[j][k] for all k
            # If we ADD edge (i,j): for each k, if adj[i][k] and adj[j][k], 
            #   codeg[i][k] and codeg[j][k] don't change (k sees same neighbors)
            #   but codeg[i][j] could change... hmm
            # Actually: codeg[a][b] = |N(a) ∩ N(b)|
            # Flipping (i,j): changes N(i) and N(j)
            # - codeg[i][k] for k != j: changes by +adj[j][k] or -adj[j][k]
            # - codeg[j][k] for k != i: changes by +adj[i][k] or -adj[i][k]
            # - codeg[i][j]: changes by... all vertices that are neighbors of both
            #   if we add edge (i,j): codeg[i][j] doesn't directly change from the flip
            #   (codeg counts common NEIGHBORS, and i,j themselves aren't counted)
            #   Wait, codeg[i][j] = |{k : adj[i][k] and adj[j][k] and k!=i and k!=j}|
            #   Flipping adj[i][j] doesn't change this!
            
            # So flipping (i,j):
            # - For each k != i,j:
            #   codeg[i][k] changes by delta_ik = +1 if adj[j][k] and adding edge, 
            #                                    -1 if adj[j][k] and removing edge
            #   codeg[j][k] changes by delta_jk = +1 if adj[i][k] and adding edge,
            #                                    -1 if adj[i][k] and removing edge
            # - codeg[i][j] doesn't change
            # - deg[i] changes by +1 or -1
            # - deg[j] changes by +1 or -1
            
            sign = 1 if not was_edge else -1  # +1 if adding, -1 if removing
            
            # Compute old violation contribution of affected pairs and new
            old_contrib = 0
            new_contrib = 0
            
            # Pair (i, j) itself
            if was_edge:
                if codeg[i][j] > n-2:
                    old_contrib += codeg[i][j] - (n-2)
            else:
                comp_cd = N - 2 - deg[i] - deg[j] + codeg[i][j]
                if comp_cd > n-1:
                    old_contrib += comp_cd - (n-1)
            
            new_deg_i = deg[i] + sign
            new_deg_j = deg[j] + sign
            
            if not was_edge:  # will become edge
                if codeg[i][j] > n-2:
                    new_contrib += codeg[i][j] - (n-2)
            else:  # will become non-edge
                comp_cd = N - 2 - new_deg_i - new_deg_j + codeg[i][j]
                if comp_cd > n-1:
                    new_contrib += comp_cd - (n-1)
            
            # Pairs (i, k) and (j, k) for k != i, j
            for k in range(N):
                if k == i or k == j:
                    continue
                
                # Pair (i, k)
                old_cd_ik = codeg[i][k]
                new_cd_ik = old_cd_ik + sign * (1 if adj[j][k] else 0)
                
                if adj[i][k]:
                    if old_cd_ik > n-2:
                        old_contrib += old_cd_ik - (n-2)
                    if new_cd_ik > n-2:
                        new_contrib += new_cd_ik - (n-2)
                else:
                    old_comp = N - 2 - deg[i] - deg[k] + old_cd_ik
                    new_comp = N - 2 - new_deg_i - deg[k] + new_cd_ik
                    if old_comp > n-1:
                        old_contrib += old_comp - (n-1)
                    if new_comp > n-1:
                        new_contrib += new_comp - (n-1)
                
                # Pair (j, k)
                old_cd_jk = codeg[j][k]
                new_cd_jk = old_cd_jk + sign * (1 if adj[i][k] else 0)
                
                if adj[j][k]:
                    if old_cd_jk > n-2:
                        old_contrib += old_cd_jk - (n-2)
                    if new_cd_jk > n-2:
                        new_contrib += new_cd_jk - (n-2)
                else:
                    old_comp = N - 2 - deg[j] - deg[k] + old_cd_jk
                    new_comp = N - 2 - new_deg_j - deg[k] + new_cd_jk
                    if old_comp > n-1:
                        old_contrib += old_comp - (n-1)
                    if new_comp > n-1:
                        new_contrib += new_comp - (n-1)
            
            delta = new_contrib - old_contrib
            
            # Accept if improvement or with small probability
            if delta <= 0 or rng.random() < 0.005:
                # Apply flip
                adj[i][j] = not adj[i][j]
                adj[j][i] = not adj[j][i]
                deg[i] += sign
                deg[j] += sign
                
                for k in range(N):
                    if k == i or k == j:
                        continue
                    if adj[j][k]:
                        codeg[i][k] += sign
                        codeg[k][i] += sign
                    if adj[i][k]:
                        codeg[j][k] += sign
                        codeg[k][j] += sign
                
                viol += delta
        
        if restart % 10 == 0:
            print(f"Restart {restart}: best_viol={viol}")
    
    return None, -1


def main():
    for n in [2, 3, 4, 5, 6, 7, 8]:
        print(f"\n=== n={n} ===")
        result, restart = search_graph(n)
        if result is not None:
            N = 4*n - 2
            adj = result
            print(f"Found at restart {restart}")
            print(f"Degrees: {sorted(set(sum(row) for row in adj))}")
            
            # Verify
            ok = True
            for i in range(N):
                for j in range(i+1, N):
                    cd = sum(1 for k in range(N) if k!=i and k!=j and adj[i][k] and adj[j][k])
                    if adj[i][j]:
                        if cd > n-2:
                            print(f"FAIL: edge ({i},{j}) codeg={cd}")
                            ok = False
                    else:
                        comp_cd = sum(1 for k in range(N) if k!=i and k!=j and not adj[i][k] and not adj[j][k])
                        if comp_cd > n-1:
                            print(f"FAIL: non-edge ({i},{j}) comp_codeg={comp_cd}")
                            ok = False
            
            if ok:
                print("Verified OK!")
                result_str = []
                for j in range(N):
                    for i in range(j):
                        result_str.append("1" if adj[i][j] else "0")
                print(f"String length: {len(result_str)}")
        else:
            print("FAILED!")


if __name__ == "__main__":
    main()
