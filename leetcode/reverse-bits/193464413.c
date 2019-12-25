// title: reverse-bits
// detail: https://leetcode.com/submissions/detail/193464413/
// datetime: Wed Dec  5 14:17:17 2018
// runtime: 4 ms
// memory: N/A

uint32_t reverseBits(uint32_t n) {
    uint32_t i = 0, one = 1, result = 0;
    for(i = 0; i < 32; i++){
        if(((one << i) & n) != 0){
            result += (one << (31 - i));
        }
    }
    return result;
}