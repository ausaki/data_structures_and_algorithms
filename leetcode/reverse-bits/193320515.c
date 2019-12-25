// title: reverse-bits
// detail: https://leetcode.com/submissions/detail/193320515/
// datetime: Tue Dec  4 20:20:35 2018
// runtime: 0 ms
// memory: 786.4 KB

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