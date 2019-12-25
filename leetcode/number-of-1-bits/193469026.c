// title: number-of-1-bits
// detail: https://leetcode.com/submissions/detail/193469026/
// datetime: Wed Dec  5 14:41:07 2018
// runtime: 0 ms
// memory: N/A

int hammingWeight(uint32_t n) {
    uint32_t i = 0, result = 0;
    for(i = 0; i < 32; i++){
        if(((1 << i) & n) != 0){
            result += 1;
        }
    }
    return result;
}