// title: concatenation-of-consecutive-binary-numbers
// detail: https://leetcode.com/submissions/detail/429224340/
// datetime: Thu Dec 10 21:37:08 2020
// runtime: 4 ms
// memory: 6.3 MB

#define MOD 1000000007

long dp[100001];
int offset = 1;

int bit_length(int n){
    int l = 0;
    while(n > 0){
        l++;
        n >>= 1;
    }
    return l;
}

int concatenatedBinary(int n){
    dp[0] = 0;
    for(;offset <= n; offset++){
        dp[offset] = ((dp[offset - 1] << bit_length(offset)) % MOD + offset) % MOD;
    }
    return dp[n];
}