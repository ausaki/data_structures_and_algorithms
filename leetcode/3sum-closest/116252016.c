// title: 3sum-closest
// detail: https://leetcode.com/submissions/detail/116252016/
// datetime: Wed Aug 30 18:45:15 2017
// runtime: 42 ms
// memory: N/A

/**
 * Return an array of arrays of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */


int cmpfunc (const void * a, const void * b){
   return ( *(int*)a - *(int*)b );
}

int abs(num){
    return num > 0 ? num : -num;
}

int threeSumClosest(int* nums, int numsSize, int target) {
    int i = 0, j, k, two_sum, sum;
    int MAX_INT = 1 << (sizeof(int) * 8 - 1) - 1;
    int result = MAX_INT;
    
    qsort(nums, numsSize, sizeof(int), cmpfunc);
    
    for(i = 0; i < numsSize; i ++){
        if(i - 1 >= 0 && nums[i] == nums[i - 1]){
            continue;
        }
        for(j = i + 1; j < numsSize; j ++){
            if(j - 1 >= i + 1 && nums[j] == nums[j - 1]){
                continue;
            }
            two_sum = nums[i] + nums[j];
            for(k = j + 1; k < numsSize; k ++){
                sum = two_sum + nums[k];
                if(abs(sum - target) < abs(result - target)){
                    result = sum;
                }
                if(sum == target){
                    return result;
                } 
                if(nums[k] >= 0 && sum > target){
                    break;
                }
            }
        }
    }
    return result;
}