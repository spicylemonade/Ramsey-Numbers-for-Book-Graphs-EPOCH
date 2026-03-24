#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 402

int N, n_val;
int adj[MAXN][MAXN];
int deg[MAXN];
int cd[MAXN][MAXN];

unsigned long long rng_state;
unsigned int rng_next() {
    rng_state ^= rng_state << 13;
    rng_state ^= rng_state >> 7;
    rng_state ^= rng_state << 17;
    return (unsigned int)(rng_state);
}
int rng_int(int bound) { return rng_next() % bound; }

void init_random_graph() {
    memset(adj, 0, sizeof(int)*MAXN*MAXN);
    memset(deg, 0, sizeof(deg));
    int target = 2 * n_val - 2;
    
    /* Add edges randomly up to target degree */
    for (int round = 0; round < 5; round++) {
        for (int i = 0; i < N; i++) {
            if (deg[i] >= target) continue;
            for (int attempt = 0; attempt < N; attempt++) {
                int j = rng_int(N);
                if (j == i || adj[i][j] || deg[j] >= target) continue;
                adj[i][j] = adj[j][i] = 1;
                deg[i]++; deg[j]++;
                if (deg[i] >= target) break;
            }
        }
    }
}

void compute_cd() {
    for (int i = 0; i < N; i++)
        for (int j = i; j < N; j++) {
            int c = 0;
            for (int k = 0; k < N; k++) c += adj[i][k] & adj[j][k];
            cd[i][j] = cd[j][i] = c;
        }
}

/* Compute violation delta for flipping edge (i,j) */
int flip_delta(int i, int j) {
    int was = adj[i][j];
    int sign = was ? -1 : 1;
    int ndi = deg[i] + sign, ndj = deg[j] + sign;
    int me = n_val - 2, mn = n_val - 1;
    int old_v = 0, new_v = 0;
    int c;
    
    /* Pair (i,j) */
    c = cd[i][j];
    if (was) {
        if (c > me) old_v += c - me;
        { int comp = N-2-ndi-ndj+c; if (comp > mn) new_v += comp - mn; }
    } else {
        { int comp = N-2-deg[i]-deg[j]+c; if (comp > mn) old_v += comp - mn; }
        if (c > me) new_v += c - me;
    }
    
    /* Pairs involving i or j */
    for (int k = 0; k < N; k++) {
        if (k == i || k == j) continue;
        int dk = deg[k];
        
        /* (i,k) */
        int cik = cd[i][k];
        int ncik = cik + sign * adj[j][k];
        if (adj[i][k]) {
            if (cik > me) old_v += cik - me;
            if (ncik > me) new_v += ncik - me;
        } else {
            int oc = N-2-deg[i]-dk+cik;
            int nc = N-2-ndi-dk+ncik;
            if (oc > mn) old_v += oc - mn;
            if (nc > mn) new_v += nc - mn;
        }
        
        /* (j,k) */
        int cjk = cd[j][k];
        int ncjk = cjk + sign * adj[i][k];
        if (adj[j][k]) {
            if (cjk > me) old_v += cjk - me;
            if (ncjk > me) new_v += ncjk - me;
        } else {
            int oc = N-2-deg[j]-dk+cjk;
            int nc = N-2-ndj-dk+ncjk;
            if (oc > mn) old_v += oc - mn;
            if (nc > mn) new_v += nc - mn;
        }
    }
    return new_v - old_v;
}

void apply_flip(int i, int j) {
    int was = adj[i][j];
    int sign = was ? -1 : 1;
    
    /* Save old adj rows before modification */
    int old_adj_j[MAXN], old_adj_i[MAXN];
    memcpy(old_adj_j, adj[j], sizeof(int)*N);
    memcpy(old_adj_i, adj[i], sizeof(int)*N);
    
    adj[i][j] = 1 - was;
    adj[j][i] = 1 - was;
    deg[i] += sign;
    deg[j] += sign;
    
    for (int k = 0; k < N; k++) {
        if (k != i) {
            cd[i][k] += sign * old_adj_j[k];
            cd[k][i] += sign * old_adj_j[k];
        }
        if (k != j) {
            cd[j][k] += sign * old_adj_i[k];
            cd[k][j] += sign * old_adj_i[k];
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) return 1;
    n_val = atoi(argv[1]);
    N = 4 * n_val - 2;
    
    if (n_val == 1) { printf("0\n"); return 0; }
    if (N > MAXN) return 1;
    
    int max_restarts = 1000;
    int max_steps = 5000000;
    
    /* Adaptive parameters based on problem size */
    if (N > 100) { max_restarts = 200; max_steps = 3000000; }
    if (N > 200) { max_restarts = 100; max_steps = 2000000; }
    
    for (int restart = 0; restart < max_restarts; restart++) {
        rng_state = 1337 + restart * 997 + n_val * 31;
        init_random_graph();
        compute_cd();
        
        int viol = 0;
        int me = n_val - 2, mn = n_val - 1;
        for (int i = 0; i < N; i++)
            for (int j = i+1; j < N; j++) {
                int c = cd[i][j];
                if (adj[i][j]) { if (c > me) viol += c - me; }
                else { int comp = N-2-deg[i]-deg[j]+c; if (comp > mn) viol += comp - mn; }
            }
        
        if (viol == 0) goto done;
        
        /* Simulated annealing with cooling */
        int temp_num = 50; /* acceptance = temp_num/1000 */
        int no_improve = 0;
        
        for (int step = 0; step < max_steps && viol > 0; step++) {
            int i = rng_int(N);
            int j = rng_int(N);
            if (i == j) continue;
            if (i > j) { int t = i; i = j; j = t; }
            
            int delta = flip_delta(i, j);
            
            if (delta <= 0 || (int)(rng_int(1000)) < temp_num) {
                apply_flip(i, j);
                viol += delta;
                
                if (delta < 0) no_improve = 0;
                else no_improve++;
            } else {
                no_improve++;
            }
            
            /* Cooling and reheating */
            if (step % 10000 == 0 && step > 0) {
                if (temp_num > 2) temp_num--;
            }
            if (no_improve > N * N) {
                temp_num = 50; /* reheat */
                no_improve = 0;
            }
        }
        
        if (viol == 0) goto done;
        if (restart % 50 == 0)
            fprintf(stderr, "n=%d restart %d: viol=%d\n", n_val, restart, viol);
    }
    
    fprintf(stderr, "FAILED for n=%d\n", n_val);
    return 1;

done:
    for (int j = 0; j < N; j++)
        for (int i = 0; i < j; i++)
            putchar('0' + adj[i][j]);
    putchar('\n');
    return 0;
}
