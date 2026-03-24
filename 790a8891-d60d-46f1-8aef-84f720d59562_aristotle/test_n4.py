"""Exhaustive search for n=4 using two-layer approach with S0 != S1."""
from itertools import combinations, product

def verify_two_layer(n, m, S0, S1, T):
    N = 4 * n - 2
    S0, S1, T = set(S0), set(S1), set(T)
    d0 = len(S0) + len(T)
    d1 = len(S1) + len(T)
    
    for d in range(1, m):
        # Within layer 0 codegree
        cd_l0 = sum(1 for s in S0 if (s + d) % m in S0) + \
                sum(1 for t in T if (t + d) % m in T)
        cd_l1 = sum(1 for s in S1 if (s + d) % m in S1) + \
                sum(1 for t in T if (t + d) % m in T)
        
        # Cross codegree: |S0 ∩ (T+d)| + |S1 ∩ (T+d)|
        # where |Sj ∩ (T+d)| = |{s in Sj : (d+s) % m in T}|... 
        # Actually need to be careful about the formula
        # Cross pair (i,0)-(i+d,1): common neighbors
        # In layer 0: s in S0, d-s in T (i.e., s in S0, s in d-T = d+T since T=-T)
        cd_cross_l0 = sum(1 for s in S0 if (d - s) % m in T)
        # In layer 1: s in S1, d+s in T
        cd_cross_l1 = sum(1 for s in S1 if (d + s) % m in T)
        cd_cross = cd_cross_l0 + cd_cross_l1

        # Layer 0 edges/non-edges
        if d in S0:
            if cd_l0 > n - 2:
                return False
        else:
            comp_cd = N - 2 - d0 - d0 + cd_l0
            if comp_cd > n - 1:
                return False

        # Layer 1 edges/non-edges
        if d in S1:
            if cd_l1 > n - 2:
                return False
        else:
            comp_cd = N - 2 - d1 - d1 + cd_l1
            if comp_cd > n - 1:
                return False

        # Cross edges/non-edges
        if d in T:
            if cd_cross > n - 2:
                return False
        else:
            comp_cd = N - 2 - d0 - d1 + cd_cross
            if comp_cd > n - 1:
                return False

    # Twin (d=0, cross pair)
    cd_twin_l0 = sum(1 for s in S0 if s in T)
    cd_twin_l1 = sum(1 for s in S1 if s in T)
    cd_twin = cd_twin_l0 + cd_twin_l1
    if 0 in T:
        if cd_twin > n - 2:
            return False
    else:
        comp_cd = N - 2 - d0 - d1 + cd_twin
        if comp_cd > n - 1:
            return False

    return True


def search_n4():
    n = 4
    m = 7
    N = 14
    
    pairs = [(k, m - k) for k in range(1, (m + 1) // 2)]
    print(f"Pairs: {pairs}")
    
    # Generate all symmetric subsets of Z_7\{0} of even size
    def all_symmetric_sets(size):
        """Generate all symmetric subsets of Z_m\{0} of given even size."""
        num_pairs_needed = size // 2
        result = []
        for combo in combinations(range(len(pairs)), num_pairs_needed):
            s = set()
            for i in combo:
                s.add(pairs[i][0])
                s.add(pairs[i][1])
            result.append(frozenset(s))
        return result
    
    # Also include T with 0 (odd size)
    def all_symmetric_sets_with_zero(size):
        """Generate all symmetric subsets including 0, of given odd size."""
        num_pairs_needed = (size - 1) // 2
        result = []
        for combo in combinations(range(len(pairs)), num_pairs_needed):
            s = {0}
            for i in combo:
                s.add(pairs[i][0])
                s.add(pairs[i][1])
            result.append(frozenset(s))
        return result
    
    # Try all valid (S0, S1, T) with |S0|+|T| = 6, |S1|+|T| = 6
    # S0, S1 are symmetric subsets of Z_m\{0} (even size)
    # T is symmetric subset of Z_m (even size, or odd if 0 in T)
    # |S0| = |S1| (for regular graph)
    
    found = False
    for s_size in [0, 2, 4, 6]:
        t_size = 6 - s_size
        if t_size < 0 or t_size > m:
            continue
        
        S0_options = all_symmetric_sets(s_size)
        S1_options = all_symmetric_sets(s_size)
        
        if t_size % 2 == 0:
            if t_size == 0:
                T_options = [frozenset()]
            else:
                T_options = all_symmetric_sets(t_size)
        else:
            T_options = all_symmetric_sets_with_zero(t_size)
        
        print(f"\nTrying s_size={s_size}, t_size={t_size}: {len(S0_options)} x {len(S1_options)} x {len(T_options)} = {len(S0_options)*len(S1_options)*len(T_options)} combos")
        
        for S0 in S0_options:
            for S1 in S1_options:
                for T in T_options:
                    if verify_two_layer(n, m, S0, S1, T):
                        print(f"  FOUND: S0={sorted(S0)}, S1={sorted(S1)}, T={sorted(T)}")
                        found = True
        
        if found:
            break
    
    if not found:
        print("\nNo solution found with regular two-layer construction!")


if __name__ == "__main__":
    search_n4()
