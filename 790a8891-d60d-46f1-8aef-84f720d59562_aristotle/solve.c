/*
 * Constructs a graph on 4n-2 vertices avoiding B_{n-1} and whose
 * complement avoids B_n.
 *
 * Method: Two-layer construction on Z_m × {0,1} where m = 2n-1.
 * Layer 0 uses connection set S0, Layer 1 uses S1, cross uses T.
 * For odd n with prime-power m ≡ 1 mod 4: Paley construction.
 * For odd n otherwise: partition search with greedy repair.
 * For even n: partition search with T using different sizes, or SA.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXM 250

int m_val, n_val, N_val;

/* GF(p) arithmetic */
int is_prime(int p) {
    if (p < 2) return 0;
    if (p < 4) return 1;
    if (p%2==0 || p%3==0) return 0;
    for (int i=5; i*i<=p; i+=6)
        if (p%i==0 || p%(i+2)==0) return 0;
    return 1;
}

int prime_power(int m, int *p_out, int *k_out) {
    /* If m = p^k for prime p, set *p_out=p, *k_out=k, return 1. Else 0. */
    for (int p = 2; p <= m; p++) {
        if (p*p > m) {
            if (is_prime(m)) { *p_out = m; *k_out = 1; return 1; }
            return 0;
        }
        if (m % p == 0) {
            if (!is_prime(p)) return 0;
            int k = 0, v = 1;
            while (v < m) { v *= p; k++; }
            if (v == m) { *p_out = p; *k_out = k; return 1; }
            return 0;
        }
    }
    return 0;
}

/* For GF(p) with p prime */
int qr_prime[MAXM]; /* 1 if QR, 0 otherwise */
int S0[MAXM], S1_arr[MAXM]; /* sets as arrays */
int nS0, nS1;
int T_set[MAXM], nT;

void compute_qr_prime(int p) {
    memset(qr_prime, 0, sizeof(qr_prime));
    for (int x = 1; x < p; x++)
        qr_prime[(x*x) % p] = 1;
}

/* Verify two-layer construction */
int verify_two_layer(int n, int m, int *s0, int ns0, int *s1, int ns1, int *t, int nt) {
    /* Build lookup sets */
    int in_s0[MAXM] = {0}, in_s1[MAXM] = {0}, in_t[MAXM] = {0};
    for (int i = 0; i < ns0; i++) in_s0[s0[i]] = 1;
    for (int i = 0; i < ns1; i++) in_s1[s1[i]] = 1;
    for (int i = 0; i < nt; i++) in_t[t[i]] = 1;
    
    int d0 = ns0 + nt, d1 = ns1 + nt;
    int N = 4*n - 2;
    
    for (int d = 1; d < m; d++) {
        /* Within layer 0 codegree */
        int cd_l0 = 0;
        for (int i = 0; i < ns0; i++)
            cd_l0 += in_s0[(s0[i] + d) % m];
        for (int i = 0; i < nt; i++)
            cd_l0 += in_t[(t[i] + d) % m];
        
        /* Within layer 1 codegree */
        int cd_l1 = 0;
        for (int i = 0; i < ns1; i++)
            cd_l1 += in_s1[(s1[i] + d) % m];
        for (int i = 0; i < nt; i++)
            cd_l1 += in_t[(t[i] + d) % m];
        
        /* Cross codegree: |S0 ∩ (T+d)| + |S1 ∩ (T+d)| */
        int cd_cross = 0;
        for (int i = 0; i < nt; i++) {
            int td = (t[i] + d) % m;
            cd_cross += in_s0[td] + in_s1[td];
        }
        /* Actually: cross codeg = |{s∈S0 : (d-s)%m ∈ T}| + |{s∈S1 : (d+s)%m ∈ T}| */
        /* Let me recompute correctly */
        cd_cross = 0;
        for (int i = 0; i < ns0; i++)
            cd_cross += in_t[(d - s0[i] + m) % m];
        for (int i = 0; i < ns1; i++)
            cd_cross += in_t[(d + s1[i]) % m];
        
        /* Check edge conditions */
        if (in_s0[d] && cd_l0 > n-2) return 0;
        if (in_s1[d] && cd_l1 > n-2) return 0;
        if (in_t[d] && cd_cross > n-2) return 0;
        
        /* Check non-edge conditions */
        if (!in_s0[d]) {
            int comp = N - 2 - d0 - d0 + cd_l0;
            if (comp > n-1) return 0;
        }
        if (!in_s1[d]) {
            int comp = N - 2 - d1 - d1 + cd_l1;
            if (comp > n-1) return 0;
        }
        if (!in_t[d]) {
            int comp = N - 2 - d0 - d1 + cd_cross;
            if (comp > n-1) return 0;
        }
    }
    
    /* Twin (d=0, cross) */
    int cd_twin = 0;
    for (int i = 0; i < ns0; i++) cd_twin += in_t[s0[i]];
    for (int i = 0; i < ns1; i++) cd_twin += in_t[s1[i]];
    if (in_t[0]) {
        if (cd_twin > n-2) return 0;
    } else {
        int comp = N - 2 - d0 - d1 + cd_twin;
        if (comp > n-1) return 0;
    }
    
    return 1;
}

void output_two_layer(int n, int m, int *s0, int ns0, int *s1, int ns1, int *t, int nt) {
    int in_s0[MAXM] = {0}, in_s1[MAXM] = {0}, in_t[MAXM] = {0};
    for (int i = 0; i < ns0; i++) in_s0[s0[i]] = 1;
    for (int i = 0; i < ns1; i++) in_s1[s1[i]] = 1;
    for (int i = 0; i < nt; i++) in_t[t[i]] = 1;
    int N = 4*n - 2;
    
    for (int j = 0; j < N; j++) {
        for (int i = 0; i < j; i++) {
            int li = i / m, pi = i % m;
            int lj = j / m, pj = j % m;
            int diff = (pj - pi + m) % m;
            int edge;
            if (li == lj) {
                edge = (li == 0) ? in_s0[diff] : in_s1[diff];
            } else {
                edge = in_t[diff];
            }
            putchar('0' + edge);
        }
    }
    putchar('\n');
}

/* RNG */
unsigned long long rng_state = 42;
unsigned int rng_next() {
    rng_state ^= rng_state << 13;
    rng_state ^= rng_state >> 7;
    rng_state ^= rng_state << 17;
    return (unsigned int)(rng_state);
}
int rng_int(int b) { return rng_next() % b; }

/* Partition search for odd n: S0 ∪ S1 = Z_m\{0}, |S0|=|S1|=n-1, T=S0 */
int partition_search_odd(int n, int m) {
    int np = (m-1)/2; /* number of pairs */
    int half = np / 2; /* pairs for S0 */
    int pairs[MAXM][2];
    for (int k = 0; k < np; k++) {
        pairs[k][0] = k + 1;
        pairs[k][1] = m - k - 1;
    }
    
    /* assignment[k] = 0 for S0, 1 for S1 */
    int assignment[MAXM];
    
    for (int attempt = 0; attempt < 2000000; attempt++) {
        rng_state = 7919 + attempt * 1009 + n * 37;
        
        /* Random assignment */
        int cnt0 = 0;
        for (int k = 0; k < np; k++) assignment[k] = 1;
        while (cnt0 < half) {
            int k = rng_int(np);
            if (assignment[k] == 1) { assignment[k] = 0; cnt0++; }
        }
        
        /* Build S0, S1, T */
        nS0 = nS1 = 0;
        for (int k = 0; k < np; k++) {
            if (assignment[k] == 0) {
                S0[nS0++] = pairs[k][0];
                S0[nS0++] = pairs[k][1];
            } else {
                S1_arr[nS1++] = pairs[k][0];
                S1_arr[nS1++] = pairs[k][1];
            }
        }
        nT = nS0;
        memcpy(T_set, S0, sizeof(int) * nS0);
        
        if (verify_two_layer(n, m, S0, nS0, S1_arr, nS1, T_set, nT)) {
            return 1;
        }
        
        /* Greedy repair: try swapping pairs */
        int improved = 1;
        while (improved) {
            improved = 0;
            for (int a = 0; a < np && !improved; a++) {
                if (assignment[a] != 0) continue;
                for (int b = 0; b < np && !improved; b++) {
                    if (assignment[b] != 1) continue;
                    /* Swap a and b */
                    assignment[a] = 1; assignment[b] = 0;
                    nS0 = nS1 = 0;
                    for (int k = 0; k < np; k++) {
                        if (assignment[k] == 0) {
                            S0[nS0++] = pairs[k][0];
                            S0[nS0++] = pairs[k][1];
                        } else {
                            S1_arr[nS1++] = pairs[k][0];
                            S1_arr[nS1++] = pairs[k][1];
                        }
                    }
                    nT = nS0;
                    memcpy(T_set, S0, sizeof(int) * nS0);
                    
                    if (verify_two_layer(n, m, S0, nS0, S1_arr, nS1, T_set, nT)) {
                        return 1;
                    }
                    
                    /* Undo */
                    assignment[a] = 0; assignment[b] = 1;
                }
            }
        }
    }
    return 0;
}

/* For even n: try various T choices with S0=S1 or S0≠S1 */
int search_even(int n, int m) {
    int np = (m-1)/2;
    int pairs[MAXM][2];
    for (int k = 0; k < np; k++) {
        pairs[k][0] = k + 1;
        pairs[k][1] = m - k - 1;
    }
    
    /* Try all possible T sizes (even) and S0=S1=S */
    /* |S| + |T| = 2n-2, |S| even, |T| even */
    for (int t_pairs = 0; t_pairs <= np && t_pairs*2 <= 2*n-2; t_pairs++) {
        int s_size = 2*n - 2 - 2*t_pairs;
        int s_pairs = s_size / 2;
        if (s_pairs + t_pairs > np) continue;
        if (s_size < 0) continue;
        
        for (int attempt = 0; attempt < 500000; attempt++) {
            rng_state = 3571 + attempt * 1013 + n * 43 + t_pairs * 997;
            
            /* Random assignment: s_pairs to S, t_pairs to T, rest unused */
            int used[MAXM];
            memset(used, 0, sizeof(used));
            nS0 = 0; nT = 0;
            int cnt = 0;
            while (cnt < s_pairs) {
                int k = rng_int(np);
                if (!used[k]) { used[k] = 1; S0[nS0++] = pairs[k][0]; S0[nS0++] = pairs[k][1]; cnt++; }
            }
            cnt = 0;
            while (cnt < t_pairs) {
                int k = rng_int(np);
                if (!used[k]) { used[k] = 2; T_set[nT++] = pairs[k][0]; T_set[nT++] = pairs[k][1]; cnt++; }
            }
            nS1 = nS0;
            memcpy(S1_arr, S0, sizeof(int) * nS0);
            
            if (verify_two_layer(n, m, S0, nS0, S1_arr, nS1, T_set, nT))
                return 1;
        }
        
        /* Also try S0 ≠ S1 */
        for (int attempt = 0; attempt < 500000; attempt++) {
            rng_state = 9973 + attempt * 2003 + n * 53 + t_pairs * 1999;
            
            /* Random T, then random S0 and S1 independently */
            int used_t[MAXM];
            memset(used_t, 0, sizeof(used_t));
            nT = 0;
            int cnt = 0;
            while (cnt < t_pairs) {
                int k = rng_int(np);
                if (!used_t[k]) { used_t[k] = 1; T_set[nT++] = pairs[k][0]; T_set[nT++] = pairs[k][1]; cnt++; }
            }
            
            /* S0: random s_pairs pairs (can overlap with T) */
            nS0 = 0; cnt = 0;
            int used_s0[MAXM];
            memset(used_s0, 0, sizeof(used_s0));
            while (cnt < s_pairs) {
                int k = rng_int(np);
                if (!used_s0[k]) { used_s0[k] = 1; S0[nS0++] = pairs[k][0]; S0[nS0++] = pairs[k][1]; cnt++; }
            }
            
            /* S1: random s_pairs pairs (can overlap with T and S0) */
            nS1 = 0; cnt = 0;
            int used_s1[MAXM];
            memset(used_s1, 0, sizeof(used_s1));
            while (cnt < s_pairs) {
                int k = rng_int(np);
                if (!used_s1[k]) { used_s1[k] = 1; S1_arr[nS1++] = pairs[k][0]; S1_arr[nS1++] = pairs[k][1]; cnt++; }
            }
            
            if (verify_two_layer(n, m, S0, nS0, S1_arr, nS1, T_set, nT))
                return 1;
        }
    }
    return 0;
}

int main(int argc, char *argv[]) {
    if (argc < 2) return 1;
    n_val = atoi(argv[1]);
    m_val = 2 * n_val - 1;
    N_val = 4 * n_val - 2;
    
    if (n_val == 1) { printf("0\n"); return 0; }
    
    /* Try Paley for odd n with prime m ≡ 1 mod 4 */
    if (n_val % 2 == 1 && n_val >= 3) {
        int p, k;
        if (prime_power(m_val, &p, &k) && m_val % 4 == 1 && k == 1) {
            /* Paley on Z_p */
            compute_qr_prime(p);
            nS0 = nS1 = 0;
            for (int d = 1; d < p; d++) {
                if (qr_prime[d]) S0[nS0++] = d;
                else S1_arr[nS1++] = d;
            }
            nT = nS0;
            memcpy(T_set, S0, sizeof(int) * nS0);
            
            if (verify_two_layer(n_val, m_val, S0, nS0, S1_arr, nS1, T_set, nT)) {
                output_two_layer(n_val, m_val, S0, nS0, S1_arr, nS1, T_set, nT);
                return 0;
            }
        }
    }
    
    /* Search for partition (odd n) */
    if (n_val % 2 == 1 && n_val >= 3) {
        if (partition_search_odd(n_val, m_val)) {
            output_two_layer(n_val, m_val, S0, nS0, S1_arr, nS1, T_set, nT);
            return 0;
        }
    }
    
    /* Search for even n */
    if (n_val % 2 == 0) {
        if (search_even(n_val, m_val)) {
            output_two_layer(n_val, m_val, S0, nS0, S1_arr, nS1, T_set, nT);
            return 0;
        }
    }
    
    fprintf(stderr, "FAILED for n=%d\n", n_val);
    return 1;
}
