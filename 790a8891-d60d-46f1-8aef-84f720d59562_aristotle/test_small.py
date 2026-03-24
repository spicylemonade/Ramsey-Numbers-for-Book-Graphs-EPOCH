"""Test small cases to understand what constructions work."""
from itertools import combinations

def auto_corr_all(S_set, N):
    """Compute auto-correlation |S ∩ (S+d)| for all d."""
    S_list = sorted(S_set)
    S_lookup = [False] * N
    for s in S_list:
        S_lookup[s] = True
    ac = [0] * N
    for s in S_list:
        for d in range(1, N):
            if S_lookup[(s + d) % N]:
                ac[d] += 1
    return ac

def check_circulant(S_set, N, n):
    """Check if circulant with connection set S works."""
    ac = auto_corr_all(S_set, N)
    for d in range(1, N):
        if d in S_set:
            if ac[d] > n - 2:
                return False, f"edge d={d}: ac={ac[d]} > {n-2}"
        else:
            if ac[d] > n - 1:
                return False, f"non-edge d={d}: ac={ac[d]} > {n-1}"
    return True, "OK"

def test_n4():
    """Exhaustive search for n=4 circulant on Z_14."""
    n = 4
    N = 14
    half = N // 2  # = 7
    pairs = [(d, N - d) for d in range(1, half)]  # 6 pairs
    print(f"n={n}, N={N}, pairs={pairs}")
    
    for combo in combinations(range(len(pairs)), n - 1):
        S = set()
        for i in combo:
            S.add(pairs[i][0])
            S.add(pairs[i][1])
        ok, msg = check_circulant(S, N, n)
        pair_desc = [pairs[i] for i in combo]
        if ok:
            print(f"  FOUND: pairs={pair_desc}, S={sorted(S)}")
            return S
        # Print failures for debugging
        # print(f"  FAIL: pairs={pair_desc}: {msg}")
    
    print("  No circulant solution found for n=4")
    return None

def test_n2():
    n = 2
    N = 6
    pairs = [(d, N - d) for d in range(1, N // 2)]
    print(f"n={n}, N={N}, pairs={pairs}")
    for combo in combinations(range(len(pairs)), n - 1):
        S = set()
        for i in combo:
            S.add(pairs[i][0])
            S.add(pairs[i][1])
        ok, msg = check_circulant(S, N, n)
        if ok:
            print(f"  FOUND: S={sorted(S)}")

def test_n3_paley():
    """Test Paley construction for n=3."""
    n = 3
    m = 5
    N = 10
    # QR mod 5: {1, 4}
    QR = {1, 4}
    QNR = {2, 3}
    S0, S1, T = QR, QNR, QR
    
    # Verify
    print(f"n={n}, m={m}, S0={S0}, S1={S1}, T={T}")
    for d in range(1, m):
        cd_l0 = sum(1 for s in S0 if (s + d) % m in S0) + sum(1 for t in T if (t + d) % m in T)
        cd_l1 = sum(1 for s in S1 if (s + d) % m in S1) + sum(1 for t in T if (t + d) % m in T)
        cd_cross = sum(1 for s in S0 if (d + s) % m in T) + sum(1 for s in S1 if (d + s) % m in T)
        
        is_edge_l0 = d in S0
        is_edge_l1 = d in S1
        is_edge_cross = d in T
        
        print(f"  d={d}: l0={cd_l0}({'E' if is_edge_l0 else 'N'}), l1={cd_l1}({'E' if is_edge_l1 else 'N'}), cross={cd_cross}({'E' if is_edge_cross else 'N'})")

if __name__ == "__main__":
    test_n2()
    print()
    test_n3_paley()
    print()
    test_n4()
