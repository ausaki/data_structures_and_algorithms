// title: two-sum-ii---input-array-is-sorted
// detail: https://leetcode.com/submissions/detail/193122796/
// datetime: Mon Dec  3 18:44:09 2018
// runtime: 0 ms
// memory: N/A

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int i = 0,
        j = numbersSize - 1,
        sum = 0;
    int* result = (int*)malloc(sizeof(int) * 2);
    
    for(;i < j;){
        sum = numbers[i] + numbers[j];
        if(sum > target){
            j--;
        }else if(sum == target){
            break;
        }else{
            i++;
        }
    }
    *returnSize = 2;
    result[0] = i + 1;
    result[1] = j + 1;
    return result;
}