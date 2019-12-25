// title: rotate-array
// detail: https://leetcode.com/submissions/detail/193312215/
// datetime: Tue Dec  4 18:20:09 2018
// runtime: 4 ms
// memory: N/A

void rotate(int* nums, int numsSize, int k) {
    int i, j, tmp;
    k = k % numsSize;
    if(k == numsSize){
        return;
    }
    for(i = 0, j = numsSize - k - 1; i < j; i++, j--){
        tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    for(i = numsSize - k, j = numsSize - 1; i < j; i++, j--){
        tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    for(i = 0, j = numsSize - 1; i < j; i++, j--){
        tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}