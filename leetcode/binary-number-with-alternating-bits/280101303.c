// title: binary-number-with-alternating-bits
// detail: https://leetcode.com/submissions/detail/280101303/
// datetime: Tue Nov 19 20:50:50 2019
// runtime: 4 ms
// memory: 6.7 MB



bool hasAlternatingBits(int n){
    unsigned int m = n ^ (n >> 1);
    return (m & (m + 1)) == 0;
}

