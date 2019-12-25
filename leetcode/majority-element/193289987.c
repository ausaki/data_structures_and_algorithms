// title: majority-element
// detail: https://leetcode.com/submissions/detail/193289987/
// datetime: Tue Dec  4 15:27:54 2018
// runtime: 4 ms
// memory: N/A

int majorityElement(int* nums, int numsSize) {
    int i, count = 0;
    int candidate = 0;
    for(i = 0; i < numsSize; i++){
        if(count == 0){
            candidate = nums[i];
        }
        count += nums[i] == candidate ? 1 : -1;
    }
    return candidate;
}