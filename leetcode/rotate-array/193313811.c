// title: rotate-array
// detail: https://leetcode.com/submissions/detail/193313811/
// datetime: Tue Dec  4 18:41:34 2018
// runtime: 4 ms
// memory: N/A

void reverse(int* nums, int start, int end){
    int tmp;
    for(; start < end; start++, end--){
        tmp = nums[start];
        nums[start] = nums[end];
        nums[end] = tmp;
    }
}

void rotate(int* nums, int numsSize, int k) {
    int i, j, tmp;
    k = k % numsSize;
    if(k == numsSize){
        return;
    }
    reverse(nums, 0, numsSize - k - 1);
    reverse(nums, numsSize - k, numsSize - 1);
    reverse(nums, 0, numsSize - 1);
}