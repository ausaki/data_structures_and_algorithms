#include <string.h>

typedef struct _fenwicktree {
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
