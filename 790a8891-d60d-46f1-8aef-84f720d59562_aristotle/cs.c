
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MN 402
static int N,nv,adj[MN][MN],deg[MN],cd[MN][MN];
static unsigned long long rs;
static int ri(int b){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return(int)((unsigned)(rs>>16)%b);}

static void init(int target){
    memset(adj,0,sizeof(adj));memset(deg,0,sizeof(deg));
    for(int r=0;r<30;r++)for(int i=0;i<N;i++){
        if(deg[i]>=target)continue;
        for(int a=0;a<N*5;a++){int j=ri(N);if(j!=i&&!adj[i][j]&&deg[j]<target){
            adj[i][j]=adj[j][i]=1;deg[i]++;deg[j]++;if(deg[i]>=target)break;}}}}

static void ccd(){for(int i=0;i<N;i++)for(int j=i;j<N;j++){
    int c=0;for(int k=0;k<N;k++)c+=adj[i][k]&adj[j][k];cd[i][j]=cd[j][i]=c;}}

static int compute_viol(int me, int mn){
    int v=0;
    for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
        int c=cd[i][j];
        if(adj[i][j]){if(c>me)v+=c-me;}
        else{int cc=N-2-deg[i]-deg[j]+c;if(cc>mn)v+=cc-mn;}}
    return v;}

int main(int ac,char**av){
    nv=atoi(av[1]);N=4*nv-2;
    if(nv==1){puts("0");return 0;}
    if(N>MN)return 1;
    int me=nv-2,mn=nv-1;
    /* For even n: use degree 2n-1 to relax complement condition */
    int target = (nv%2==0) ? 2*nv-1 : 2*nv-2;
    
    for(int restart=0;restart<10000;restart++){
        rs=31337+(unsigned long long)restart*10007+(unsigned long long)nv*999983;
        init(target);ccd();
        int viol=compute_viol(me,mn);
        if(!viol)goto done;
        int temp=200,noimp=0;
        for(int step=0;step<30000000&&viol>0;step++){
            int i=ri(N),j=ri(N);
            if(i==j)continue;if(i>j){int t=i;i=j;j=t;}
            int was=adj[i][j],sign=was?-1:1;
            int ndi=deg[i]+sign,ndj=deg[j]+sign;
            int ov=0,nw=0;
            int c=cd[i][j];
            if(was){if(c>me)ov+=c-me;{int cc=N-2-ndi-ndj+c;if(cc>mn)nw+=cc-mn;}}
            else{{int cc=N-2-deg[i]-deg[j]+c;if(cc>mn)ov+=cc-mn;}if(c>me)nw+=c-me;}
            for(int k=0;k<N;k++){
                if(k==i||k==j)continue;int dk=deg[k];
                int ci=cd[i][k],ni=ci+sign*adj[j][k];
                if(adj[i][k]){if(ci>me)ov+=ci-me;if(ni>me)nw+=ni-me;}
                else{int o=N-2-deg[i]-dk+ci,n2=N-2-ndi-dk+ni;if(o>mn)ov+=o-mn;if(n2>mn)nw+=n2-mn;}
                int cj=cd[j][k],nj=cj+sign*adj[i][k];
                if(adj[j][k]){if(cj>me)ov+=cj-me;if(nj>me)nw+=nj-me;}
                else{int o=N-2-deg[j]-dk+cj,n2=N-2-ndj-dk+nj;if(o>mn)ov+=o-mn;if(n2>mn)nw+=n2-mn;}}
            int d=nw-ov;
            if(d<=0||ri(1000)<temp){
                int oi[MN],oj[MN];memcpy(oi,adj[i],N*4);memcpy(oj,adj[j],N*4);
                adj[i][j]=1-was;adj[j][i]=1-was;deg[i]=ndi;deg[j]=ndj;
                for(int k=0;k<N;k++){
                    if(k!=i){cd[i][k]+=sign*oj[k];cd[k][i]+=sign*oj[k];}
                    if(k!=j){cd[j][k]+=sign*oi[k];cd[k][j]+=sign*oi[k];}}
                viol+=d;if(d<0)noimp=0;else noimp++;}
            else noimp++;
            if(step%200000==0&&step>0&&temp>5)temp-=3;
            if(noimp>N*N*5){temp=200+ri(100);noimp=0;}}
        if(!viol)goto done;
        if(restart%100==0)fprintf(stderr,"n=%d r=%d v=%d\n",nv,restart,viol);
    }
    return 1;
done:
    for(int j=0;j<N;j++)for(int i=0;i<j;i++)putchar('0'+adj[i][j]);
    putchar('\n');return 0;
}
