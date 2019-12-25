// title: 3sum
// detail: https://leetcode.com/submissions/detail/116193629/
// datetime: Wed Aug 30 10:55:16 2017
// runtime: 249 ms
// memory: N/A

/**
 * Return an array of arrays of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */


int cmpfunc (const void * a, const void * b){
   return ( *(int*)a - *(int*)b );
}

/*
 * 二分查找
 */
int bifind(int* nums, int size, int target){
    int l, r, m;
    l = 0;
    r = size - 1;
    if(r < 0){
        return -1;
    }
    while(l < r){
        m = l + (r - l) / 2;
        if(nums[m] == target){
            return m;
        } else if(nums[m] > target){
            r = m - 1;
        } else {
            l = m + 1;
        }
    }
    if(nums[l] == target){
        return l;
    } else {
        return -1;
    }
}

/*
 * 
 */
int** threeSum(int* nums, int numsSize, int* returnSize) {
    int row_size = 20;
    int i = 0, j, k, delta;
    int size = 0;
    int* p0 = NULL;
    int* p1 = NULL;
    int** result = (int**)malloc(sizeof(int*) * row_size);
    int row = 0;
    
    qsort(nums, numsSize, sizeof(int), cmpfunc);
    
    for(i = 0; i < numsSize - 1; i ++){
        if(i - 1 >= 0 && nums[i - 1] == nums[i]){
            continue;
        }
        for(j = i + 1; j < numsSize; j ++){
            delta = nums[i] + nums[j];
            if(j - 1 >= i + 1 && nums[j - 1] == nums[j]){
                continue;
            }
            p0 = nums + j + 1;
            size = numsSize - j - 1;
            k = bifind(p0, size, -delta);
            if(k >= 0){
                // 找到了
                p1 = (int*)malloc(sizeof(int) * 3);
                p1[0] = nums[i];
                p1[1] = nums[j];
                p1[2] = p0[k];
                if(row >= row_size){
                    row_size += 10;
                    result = (int**)realloc(result, sizeof(int*) * row_size);
                }
                result[row ++] = p1;
            }
        }
    }
    *returnSize = row;
    return result;
}