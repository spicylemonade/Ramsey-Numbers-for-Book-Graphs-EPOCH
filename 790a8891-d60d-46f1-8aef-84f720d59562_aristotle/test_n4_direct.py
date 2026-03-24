"""Direct search for n=4 graph using local search on adjacency matrix."""
import random

def search_n4():
    n = 4
    N = 14
    rng = random.Random(42)
    
    # Represent graph as adjacency set
    # We want roughly (2n-2)-regular = 6-regular
    
    best_adj = None
    best_viol = float('inf')
    
    for restart in range(50):
        # Start with a random 6-regular-ish graph
        adj = [[False]*N for _ in range(N)]
        deg = [0]*N
        
        # Add edges randomly targeting degree 6
        all_edges = [(i,j) for i in range(N) for j in range(i+1,N)]
        rng.shuffle(all_edges)
        for i,j in all_edges:
            if deg[i] < 6 and deg[j] < 6:
                adj[i][j] = adj[j][i] = True
                deg[i] += 1
                deg[j] += 1
        
        def codegree(u, v):
            return sum(1 for w in range(N) if w!=u and w!=v and adj[u][w] and adj[v][w])
        
        def comp_codegree(u, v):
            return sum(1 for w in range(N) if w!=u and w!=v and not adj[u][w] and not adj[v][w])
        
        def violation():
            v = 0
            for i in range(N):
                for j in range(i+1, N):
                    if adj[i][j]:
                        cd = codegree(i, j)
                        if cd > n-2:
                            v += (cd - (n-2))**2
                    else:
                        cd = comp_codegree(i, j)
                        if cd > n-1:
                            v += (cd - (n-1))**2
            return v
        
        viol = violation()
        
        # Local search: flip edges to reduce violation
        for step in range(50000):
            if viol == 0:
                break
            
            # Pick random edge to flip
            i = rng.randint(0, N-1)
            j = rng.randint(0, N-1)
            if i == j:
                continue
            if i > j:
                i, j = j, i
            
            # Flip
            adj[i][j] = not adj[i][j]
            adj[j][i] = not adj[j][i]
            
            new_viol = violation()
            if new_viol <= viol:
                viol = new_viol
            else:
                # Undo with some probability (simulated annealing)
                if rng.random() < 0.01:
                    viol = new_viol
                else:
                    adj[i][j] = not adj[i][j]
                    adj[j][i] = not adj[j][i]
        
        if viol < best_viol:
            best_viol = viol
            best_adj = [row[:] for row in adj]
            print(f"Restart {restart}: viol={viol}, deg={[sum(row) for row in adj]}")
        
        if viol == 0:
            print(f"Found solution at restart {restart}!")
            # Print some info
            print(f"Degrees: {[sum(row) for row in adj]}")
            
            # Build adjacency string
            result = []
            for j in range(N):
                for i in range(j):
                    result.append("1" if adj[i][j] else "0")
            adj_str = "".join(result)
            print(f"Adjacency string: {adj_str}")
            
            # Verify
            for i in range(N):
                for j in range(i+1, N):
                    if adj[i][j]:
                        cd = codegree(i, j)
                        assert cd <= n-2, f"Edge ({i},{j}) codeg={cd}"
                    else:
                        cd = comp_codegree(i, j)
                        assert cd <= n-1, f"Non-edge ({i},{j}) comp_codeg={cd}"
            print("Verified OK!")
            return adj_str
    
    print(f"Best violation: {best_viol}")
    return None

if __name__ == "__main__":
    search_n4()
