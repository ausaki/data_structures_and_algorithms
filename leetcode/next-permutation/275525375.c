// title: next-permutation
// detail: https://leetcode.com/submissions/detail/275525375/
// datetime: Sun Nov  3 13:30:24 2019
// runtime: 8 ms
// memory: 7.4 MB

void nextPermutation(int* nums, int numsSize) {
    int i, j, tmp;
    
    for(i = numsSize - 2; i >= 0 && nums[i] >= nums[i + 1]; i --){}
    if(i >= 0){
        // 找到idnex的右边比nums[index]大且最接近的元素
        for(j = numsSize - 1; nums[j] <= nums[i]; j --){} 
        // 替换index1 和 index2
        tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }    
    // 倒置index1 右边的元素
    for(i ++, j = numsSize - 1; i < j; i++, j--){
        tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}