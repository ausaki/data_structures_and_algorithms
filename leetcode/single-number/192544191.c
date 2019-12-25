// title: single-number
// detail: https://leetcode.com/submissions/detail/192544191/
// datetime: Fri Nov 30 14:18:09 2018
// runtime: 4 ms
// memory: N/A

int singleNumber(int* nums, int numsSize) {
    int n = 0;
    for(int i = 0; i < numsSize; i++){
        n ^= nums[i];
    }
    return n;
}