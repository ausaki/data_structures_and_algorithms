#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int M = 100000000;
int PRIMES = 5000000;
unsigned char *bools;
int *primes;

void gen_primes(){
    int pi = 0;
    int i, j;
    bools = (unsigned char *)malloc(M / 8);
    memset(bools, (char)0xff, M / 8);
    primes = (int *)malloc(PRIMES * sizeof(int));
    for(i = 2; i < (int)sqrt(M) + 1; i++){
        if(bools[i / 8] >> (i % 8) & 1){
            primes[pi++] = i;
            for(j = i * i; j < M; j += i){
                bools[j / 8] &= ~(1 << (j % 8));
            }
        }
    }
    for(;i < M & pi < PRIMES; i++){
        if(bools[i / 8] >> (i % 8) & 1){
            primes[pi++] = i;
        }
    }
}


int main(){
    gen_primes();
    int t, k;
    scanf("%d\n", &t);
    for(int i = 0; i < t; i++){
        scanf("%d\n", &k);
        printf("%d\n", primes[k - 1]);
    }
    free(bools);
    free(primes);
    return 0;
}