// title: find-first-and-last-position-of-element-in-sorted-array
// detail: https://leetcode.com/submissions/detail/126402036/
// datetime: Thu Nov  2 10:38:14 2017
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
    
    for(i = 0, j = numsSize - 1; i <= j;){
        printf("i = %d, j = %d\n", i, j);
        if(result[0] == -1 && nums[i] == target){
            result[0] = i;
        }
        if(result[1] == -1 && nums[j] == target){
            result[1] = j;
        }
        if(result[0] != -1 && result[1] != -1){
            break;
        }
        if(result[0] == -1){
            i ++;
        }
        if(result[1] == -1){
            j --;
        }
    }
    return result;
}