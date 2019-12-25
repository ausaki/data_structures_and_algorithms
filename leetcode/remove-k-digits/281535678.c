// title: remove-k-digits
// detail: https://leetcode.com/submissions/detail/281535678/
// datetime: Mon Nov 25 16:10:33 2019
// runtime: 128 ms
// memory: 7.1 MB

#include <stdlib.h>

char * removeKdigits(char * num, int k){
    int N = strlen(num);
    int i = 0, j;
    while(i < N - 1 && k > 0){
        if(num[i] <= num[i + 1]){
            i ++;
            continue;
        }
        k -= 1;
        for(j = i + 1; j < N; j++){
            num[j - 1] = num[j];
        }
        N--;
        i--;
        if(i < 0) i = 0;
    }
    if(k > 0){
        N -= k;
        if(N < 0) N = 0;
    }
    num[N] = 0;
    while(num[0] == '0'){
        num++;
        N--;
    }
    if(N == 0){
        return "0";
    }
    num[N] = 0;
    return num;
}

