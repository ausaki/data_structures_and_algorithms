// title: single-number-iii
// detail: https://leetcode.com/submissions/detail/192728042/
// datetime: Sat Dec  1 19:06:59 2018
// runtime: 4 ms
// memory: N/A

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int ab = 0,
        a = 0, 
        b = 0, 
        i = 0,
        *result = (int*)malloc(sizeof(int) * 2);
    for(i = 0; i < numsSize; i++){
        ab ^= nums[i];
    }
    ab = ab & (-ab);
    for(i = 0; i < numsSize; i++){
        if(nums[i] & ab){
            a ^= nums[i];
        }else{
            b ^= nums[i];
        }
    }
    result[0] = a;
    result[1] = b;
    *returnSize = 2;
    return result;
}