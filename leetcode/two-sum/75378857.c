// title: two-sum
// detail: https://leetcode.com/submissions/detail/75378857/
// datetime: Thu Sep 22 23:02:57 2016
// runtime: 176 ms
// memory: N/A

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int startIdx = 0, i = 0, j = 0, ii, jj;
    int* result = (int*) malloc(sizeof(int) * 2);
    if(numsSize % 2 == 0){
        // 长度为偶数
        for(i = 0, j = 1; i <= numsSize - 2 && j <= numsSize - 1; i = i + 2, j = j + 2){
            for(ii = i + 1, jj = j + 1; ii <= numsSize - 1 && jj <= numsSize; ii ++, jj ++){
                if(nums[i] + nums[ii] == target){
                    result[0] = i;
                    result[1] = ii;
                    return result;
                } else if(jj < numsSize && nums[j] + nums[jj] == target){
                    result[0] = j;
                    result[1] = jj;
                    return result;
                }
            }
            
        }
    } else{
        // 长度为奇数
        for(i = 0, j = 1; i <= numsSize - 2 && j <= numsSize - 1; i = i + 2, j = j + 2){
            for(ii = i + 1, jj = j + 1; ii <= numsSize - 1 && jj <= numsSize; ii ++, jj ++){
                if(nums[i] + nums[ii] == target){
                    result[0] = i;
                    result[1] = ii;
                    return result;
                } else if(jj < numsSize && nums[j] + nums[jj] == target){
                    result[0] = j;
                    result[1] = jj;
                    return result;
                }
            }
        }
        
    }
    
    
    return result;
}