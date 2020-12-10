// title: concatenation-of-consecutive-binary-numbers
// detail: https://leetcode.com/submissions/detail/429220435/
// datetime: Thu Dec 10 21:17:22 2020
// runtime: 56 ms
// memory: 5.6 MB

int bit_length(int n){
    int l = 0;
    while(n > 0){
        l++;
        n >>= 1;
    }
    return l;
}

int concatenatedBinary(int n){
    int i;
    int MOD = 1000000007;
    uint64_t res = 0;
    for(int i = 1; i <= n; i++){
        res = ((res << bit_length(i)) % MOD + i) % MOD;
    }
    return res;
}