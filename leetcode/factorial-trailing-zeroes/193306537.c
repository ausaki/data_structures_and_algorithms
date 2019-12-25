// title: factorial-trailing-zeroes
// detail: https://leetcode.com/submissions/detail/193306537/
// datetime: Tue Dec  4 17:18:32 2018
// runtime: 8 ms
// memory: N/A

int trailingZeroes(int n) {
    long long i = 5;
    int result = 0;
    for(i = 5; n / i > 0; i *= 5){
        result += n / i;
    }
    return result;
}