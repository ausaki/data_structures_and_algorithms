// title: count-primes
// detail: https://leetcode.com/submissions/detail/193988848/
// datetime: Sat Dec  8 17:46:35 2018
// runtime: 8 ms
// memory: 3.8 MB

int countPrimes(int n) {
    if(n < 3){
        return 0;
    }
    bool *table = (bool*)malloc(sizeof(bool) * n);
    int i, j, result;
    table[0] = false;
    table[1] = false;
    for(i = 2; i < n; i++){
        table[i] = true;
    }
    for(i = 2; i * i < n; i++){
        if(table[i]){
            for(j = i * i; j < n; j += i){
                table[j] = false;
            }    
        }
    }
    result = 0;
    for(i = 2; i < n; i++){
        result += table[i] ? 1 : 0;
    }
    free(table);
    return result;
}