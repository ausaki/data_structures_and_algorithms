// title: two-sum
// detail: https://leetcode.com/submissions/detail/75376274/
// datetime: Thu Sep 22 22:34:32 2016
// runtime: 246 ms
// memory: N/A

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int startIdx = 0, i = 0, j = 0;
    int* result = (int*) malloc(sizeof(int) * 2);
    for(i = 0; i <= numsSize - 2; i++){
        for(j = i + 1; j <= numsSize - 1; j ++){
            if(*(nums + i) + *(nums + j) == target){
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }
    return result;
}