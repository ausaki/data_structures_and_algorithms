#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct T {
    int *bit;
    int n;
} FenwickTree;

void ft_init(FenwickTree *ft, int n){
    ft->n = n + 1;
    int sz = ft->n * sizeof(int);
    ft->bit = (int*)malloc(sz);
    memset(ft->bit, 0, sz);
}

void ft_add(FenwickTree *ft, int i, int delta){
    i++;
    while(i < ft->n){
        ft->bit[i] += delta;
        i += i & -i;
    }
}

int ft_sum(FenwickTree *ft, int i){
    i++;
    int s = 0;
    while(i > 0){
        s += ft->bit[i];
        i &= i - 1;
    }
    return s;
}

int ft_range_sum(FenwickTree *ft, int l, int r){
    return ft_sum(ft, r) - ft_sum(ft, l - 1);
}

void ft_free(FenwickTree *ft){
    free(ft->bit);
}

int* solution(int n){
    int *cards = (int*)malloc(n * sizeof(int));
    FenwickTree ft;
    ft_init(&ft, n);
    int i = 0, l, r, threshold;
    for(int j = 1; j < n + 1; j++){
        l = 0;
        r = n - 1;
        threshold = (j + 1) % (n - j + 1);
        if(threshold == 0){
            threshold = n - j + 1;
        }
        while(l <= r){
            int m = (l + r) / 2;
            int k = (i + m) % n;
            int removed = k >= i ? ft_range_sum(&ft, i, k) : j - 1 - ft_range_sum(&ft, k + 1, i - 1);
            int t = m + 1 - removed;
            if(t < threshold){
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        i = (i + l) % n;
        ft_add(&ft, i, 1);
        cards[i] = j;
        i = (i + 1) % n;
    }
    ft_free(&ft);
    return cards;
}

    
void main(){
    int t, i, n;
    scanf("%d\n", &t);
    for(i = 0; i < t; i ++){
        scanf("%d\n", &n);
        int *cards = solution(n);
        for(int j = 0; j < n; j++){
            printf("%d ", cards[j]);
        }
        free(cards);
        printf("\n");
    }
}