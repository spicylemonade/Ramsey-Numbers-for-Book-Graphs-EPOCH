"""Fast search for n=4."""
import random

def search_n(n, max_restarts=100, max_steps=100000):
    N = 4*n-2
    rng = random.Random(42+n)
    
    for restart in range(max_restarts):
        adj = [0]*N  # bitmask adjacency
        deg = [0]*N
        
        target = 2*n-2
        edges = [(i,j) for i in range(N) for j in range(i+1,N)]
        rng.shuffle(edges)
        for i,j in edges:
            if deg[i] < target and deg[j] < target:
                adj[i] |= (1<<j)
                adj[j] |= (1<<i)
                deg[i] += 1
                deg[j] += 1
        
        def cd(u,v):
            return bin(adj[u] & adj[v]).count('1')
        
        def comp_cd(u,v):
            mask = ((1<<N)-1) ^ (1<<u) ^ (1<<v)
            return bin((~adj[u] & ~adj[v]) & mask).count('1')
        
        def violation():
            v = 0
            for i in range(N):
                for j in range(i+1,N):
                    if (adj[i]>>j)&1:
                        c = cd(i,j)
                        if c > n-2:
                            v += c-(n-2)
                    else:
                        c = comp_cd(i,j)
                        if c > n-1:
                            v += c-(n-1)
            return v
        
        viol = violation()
        if viol == 0:
            return adj, N
        
        for step in range(max_steps):
            i = rng.randint(0,N-1)
            j = rng.randint(0,N-1)
            if i==j: continue
            if i>j: i,j = j,i
            
            # Flip
            adj[i] ^= (1<<j)
            adj[j] ^= (1<<i)
            
            new_viol = violation()
            if new_viol <= viol:
                viol = new_viol
                if viol == 0:
                    return adj, N
            else:
                if rng.random() < 0.01:
                    viol = new_viol
                else:
                    adj[i] ^= (1<<j)
                    adj[j] ^= (1<<i)
        
        if restart % 10 == 0:
            print(f"  restart {restart}: viol={viol}")
    
    return None, N

for n in range(1, 9):
    print(f"n={n}:")
    N = 4*n-2
    if n == 1:
        print("  trivial: '0'")
        continue
    result, N = search_n(n, max_restarts=30, max_steps=50000)
    if result:
        # verify
        adj = result
        ok = True
        for i in range(N):
            for j in range(i+1,N):
                c = bin(adj[i]&adj[j]).count('1')
                if (adj[i]>>j)&1:
                    if c > n-2: ok = False
                else:
                    mask = ((1<<N)-1)^(1<<i)^(1<<j)
                    cc = bin((~adj[i]&~adj[j])&mask).count('1')
                    if cc > n-1: ok = False
        print(f"  found! verified={ok}")
    else:
        print(f"  FAILED")
