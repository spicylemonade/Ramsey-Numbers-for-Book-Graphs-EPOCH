#include <stdio.h>
#include <string.h>
#define M 21
#define N_VAL 11
int main() {
    int pairs[10][2], np = 0;
    for (int k = 1; k <= 10; k++) { pairs[np][0]=k; pairs[np][1]=M-k; np++; }
    int n = N_VAL;
    
    // Enumerate partition masks (S0 gets half=5 pairs)
    for (int pmask = 0; pmask < (1<<np); pmask++) {
        if (__builtin_popcount(pmask) != 5) continue;
        
        int in_s0[M]={0}, in_s1[M]={0};
        for (int k=0;k<np;k++){
            if(pmask&(1<<k)){in_s0[pairs[k][0]]=in_s0[pairs[k][1]]=1;}
            else{in_s1[pairs[k][0]]=in_s1[pairs[k][1]]=1;}
        }
        
        // Enumerate T masks (5 pairs from 10)
        for (int tmask = 0; tmask < (1<<np); tmask++) {
            if (__builtin_popcount(tmask) != 5) continue;
            
            int in_t[M]={0};
            for(int k=0;k<np;k++)
                if(tmask&(1<<k)){in_t[pairs[k][0]]=in_t[pairs[k][1]]=1;}
            
            int ok = 1;
            for (int d=1;d<M&&ok;d++){
                int ad=0,bd=0,td=0;
                for(int s=1;s<M;s++){
                    if(in_s0[s]&&in_s0[(s+d)%M])ad++;
                    if(in_s1[s]&&in_s1[(s+d)%M])bd++;
                    if(in_t[s]&&in_t[(s+d)%M])td++;
                }
                if(in_s0[d]){if(ad+td>n-2)ok=0;}
                if(in_s1[d]){if(bd+td>n-2)ok=0;}
                // Non-edge checks
                if(!in_s0[d]&&d!=0){if(ad+td>n-1)ok=0;}
                if(!in_s1[d]&&d!=0){if(bd+td>n-1)ok=0;}
            }
            
            if(ok){
                printf("FOUND pmask=%d tmask=%d\n",pmask,tmask);
                printf("S0: "); for(int d=1;d<M;d++)if(in_s0[d])printf("%d ",d); printf("\n");
                printf("S1: "); for(int d=1;d<M;d++)if(in_s1[d])printf("%d ",d); printf("\n");
                printf("T:  "); for(int d=1;d<M;d++)if(in_t[d])printf("%d ",d); printf("\n");
                return 0;
            }
        }
    }
    printf("No solution found\n");
    return 0;
}
