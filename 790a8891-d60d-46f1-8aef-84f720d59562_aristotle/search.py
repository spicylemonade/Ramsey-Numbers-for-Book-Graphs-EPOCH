"""Efficient graph search using bitmask adjacency."""
import random

def popcount(x):
    return bin(x).count('1')

def search_graph(n, seed=42, max_restarts=200, max_steps=300000):
    N = 4*n - 2
    rng = random.Random(seed + n)
    target_deg = 2*n - 2
    full_mask = (1 << N) - 1
    
    best_viol = float('inf')
    best_adj = None
    
    for restart in range(max_restarts):
        # Random graph targeting degree target_deg
        adj = [0]*N
        deg = [0]*N
        edges = [(i,j) for i in range(N) for j in range(i+1,N)]
        rng.shuffle(edges)
        for i,j in edges:
            if deg[i] < target_deg and deg[j] < target_deg:
                adj[i] |= (1<<j)
                adj[j] |= (1<<i)
                deg[i] += 1
                deg[j] += 1
        
        def violation():
            v = 0
            for i in range(N):
                for j in range(i+1, N):
                    cd = popcount(adj[i] & adj[j])
                    if (adj[i] >> j) & 1:  # edge
                        if cd > n-2:
                            v += cd - (n-2)
                    else:  # non-edge
                        # complement codeg = N-2-deg[i]-deg[j]+cd
                        comp_cd = N - 2 - deg[i] - deg[j] + cd
                        if comp_cd > n-1:
                            v += comp_cd - (n-1)
            return v
        
        viol = violation()
        if viol == 0:
            return adj, deg, restart
        
        for step in range(max_steps):
            i = rng.randint(0, N-1)
            j = rng.randint(0, N-1)
            if i == j: continue
            if i > j: i, j = j, i
            
            bit_j = 1 << j
            bit_i = 1 << i
            was_edge = (adj[i] >> j) & 1
            sign = -1 if was_edge else 1
            
            # Compute violation change for affected pairs
            old_v = 0
            new_v = 0
            
            new_deg_i = deg[i] + sign
            new_deg_j = deg[j] + sign
            
            # Pair (i,j) itself
            cd_ij = popcount(adj[i] & adj[j])
            if was_edge:
                if cd_ij > n-2: old_v += cd_ij - (n-2)
                # becomes non-edge
                comp_cd = N - 2 - new_deg_i - new_deg_j + cd_ij
                if comp_cd > n-1: new_v += comp_cd - (n-1)
            else:
                comp_cd = N - 2 - deg[i] - deg[j] + cd_ij
                if comp_cd > n-1: old_v += comp_cd - (n-1)
                # becomes edge
                if cd_ij > n-2: new_v += cd_ij - (n-2)
            
            # Pairs (i,k) for k != i,j
            for k in range(N):
                if k == i or k == j: continue
                cd_ik = popcount(adj[i] & adj[k])
                new_cd_ik = cd_ik + sign * ((adj[j] >> k) & 1)
                
                is_edge_ik = (adj[i] >> k) & 1 if k > i else (adj[k] >> i) & 1
                if is_edge_ik:
                    if cd_ik > n-2: old_v += cd_ik - (n-2)
                    if new_cd_ik > n-2: new_v += new_cd_ik - (n-2)
                else:
                    old_comp = N - 2 - deg[i] - deg[k] + cd_ik
                    new_comp = N - 2 - new_deg_i - deg[k] + new_cd_ik
                    if old_comp > n-1: old_v += old_comp - (n-1)
                    if new_comp > n-1: new_v += new_comp - (n-1)
                
                # Pairs (j,k)
                cd_jk = popcount(adj[j] & adj[k])
                new_cd_jk = cd_jk + sign * ((adj[i] >> k) & 1)
                
                is_edge_jk = (adj[j] >> k) & 1 if k > j else (adj[k] >> j) & 1
                if is_edge_jk:
                    if cd_jk > n-2: old_v += cd_jk - (n-2)
                    if new_cd_jk > n-2: new_v += new_cd_jk - (n-2)
                else:
                    old_comp = N - 2 - deg[j] - deg[k] + cd_jk
                    new_comp = N - 2 - new_deg_j - deg[k] + new_cd_jk
                    if old_comp > n-1: old_v += old_comp - (n-1)
                    if new_comp > n-1: new_v += new_comp - (n-1)
            
            delta = new_v - old_v
            
            accept = delta <= 0 or rng.random() < 0.005
            if accept:
                adj[i] ^= bit_j
                adj[j] ^= bit_i
                deg[i] = new_deg_i
                deg[j] = new_deg_j
                viol += delta
                
                if viol == 0:
                    return adj, deg, restart
        
        if viol < best_viol:
            best_viol = viol
            best_adj = adj[:]
            if restart % 20 == 0:
                print(f"  n={n} restart {restart}: viol={viol}")
    
    return None, None, -1


def adj_to_string(adj, N):
    result = []
    for j in range(N):
        for i in range(j):
            result.append("1" if (adj[i] >> j) & 1 else "0")
    return "".join(result)


def verify(adj, n, N):
    deg = [popcount(a) for a in adj]
    for i in range(N):
        for j in range(i+1, N):
            cd = popcount(adj[i] & adj[j])
            if (adj[i] >> j) & 1:
                if cd > n-2:
                    return False, f"edge ({i},{j}) cd={cd}"
            else:
                comp_cd = N-2-deg[i]-deg[j]+cd
                if comp_cd > n-1:
                    return False, f"non-edge ({i},{j}) comp_cd={comp_cd}"
    return True, "OK"


if __name__ == "__main__":
    for n in range(1, 12):
        N = 4*n - 2
        if n == 1:
            print(f"n=1: trivial")
            continue
        print(f"n={n} (N={N}):")
        adj, deg, restart = search_graph(n, max_restarts=50, max_steps=100000)
        if adj is not None:
            ok, msg = verify(adj, n, N)
            s = adj_to_string(adj, N)
            print(f"  Found at restart {restart}, verified={ok} ({msg}), len={len(s)}")
        else:
            print(f"  FAILED")
