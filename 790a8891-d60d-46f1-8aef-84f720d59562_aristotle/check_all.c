#include <stdio.h>
#include <string.h>
// Exhaustive check for n=11, m=21
#define M 21
int main() {
    int pairs[10][2], np = 0;
    for (int k = 1; k <= 10; k++) { pairs[np][0] = k; pairs[np][1] = M - k; np++; }
    
    int best = 99999;
    for (int mask = 0; mask < (1 << np); mask++) {
        if (__builtin_popcount(mask) != 5) continue;
        
        int in_s0[M] = {0};
        for (int k = 0; k < np; k++) {
            if (mask & (1 << k)) {
                in_s0[pairs[k][0]] = in_s0[pairs[k][1]] = 1;
            }
        }
        
        int viol = 0;
        for (int d = 1; d < M; d++) {
            int ad = 0;
            for (int s = 1; s < M; s++) {
                if (in_s0[s] && in_s0[(s + d) % M]) ad++;
            }
            if (in_s0[d]) {
                if (2 * ad > 9) viol += 2*ad - 9;
            }
        }
        
        if (viol == 0) {
            // Full check
            int ok = 1;
            for (int d = 1; d < M && ok; d++) {
                int ad = 0, bd = 0;
                for (int s = 1; s < M; s++) {
                    if (in_s0[s] && in_s0[(s+d)%M]) ad++;
                    if (!in_s0[s] && !in_s0[(s+d)%M] && (s+d)%M != 0) bd++;
                }
                if (in_s0[d]) { if (2*ad > 9) ok = 0; }
                else { if (ad + bd > 9) ok = 0; }
            }
            if (ok) {
                printf("FOUND mask=%d\n", mask);
                for (int k = 0; k < np; k++) {
                    if (mask & (1<<k)) printf("S0: %d,%d  ", pairs[k][0], pairs[k][1]);
                }
                printf("\n");
                return 0;
            }
        }
        if (viol < best) best = viol;
    }
    printf("No solution found, best viol = %d\n", best);
    return 0;
}
