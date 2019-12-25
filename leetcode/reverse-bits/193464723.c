// title: reverse-bits
// detail: https://leetcode.com/submissions/detail/193464723/
// datetime: Wed Dec  5 14:18:47 2018
// runtime: 4 ms
// memory: N/A

uint32_t reverseBits(uint32_t n) {
    uint32_t i = 0, j = 31, b1, b2, one = 1;
    for(; i < j; i++, j--){
        b1 = ((one << i) & n) >> i;
        b2 = ((one << j) & n) >> j;
        if(b1 == 1 && b2 == 0){
            n = n & ~(one << i);
            n = n | (one << j);
        } else if(b1 == 0 && b2 == 1){
            n = n | (one << i);
            n = n & ~(one << j);
        }
    }
    return n;
}