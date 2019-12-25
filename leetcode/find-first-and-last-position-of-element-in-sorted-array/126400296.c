// title: find-first-and-last-position-of-element-in-sorted-array
// detail: https://leetcode.com/submissions/detail/126400296/
// datetime: Thu Nov  2 10:27:13 2017
// runtime: 9 ms
// memory: N/A

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int bi_search(int* nums, int start, int end, int target){
    int m;
    if(start > end){
        return -1;
    }
    m = (start + end) / 2;
    if(nums[m] == target){
        return m;
    }
    if(nums[m] > target){
        return bi_search(nums, start, m - 1, target);
    }
    return bi_search(nums, m + 1, end, target);
}

int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(sizeof(int) * 2);
    int i, j, index = -1;
    result[0] = -1;
    result[1] = -1;
    *returnSize = 2;
    
    index = bi_search(nums, 0, numsSize - 1, target);
    if(index == -1){
        result[0] = -1;
        result[1] = -1;
        return result;
    }
    for(i = index - 1; i >= 0; i --){
        if(nums[i] != target){
            break;
        }
    }
    result[0] = i + 1;
    for(j = index + 1; j < numsSize; j ++){
        if(nums[j] != target){
            break;
        }
    }
    result[1] = j - 1;
    return result;
}