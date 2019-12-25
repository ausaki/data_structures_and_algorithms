// title: permutations
// detail: https://leetcode.com/submissions/detail/142935597/
// datetime: Thu Mar  1 17:06:48 2018
// runtime: 24 ms
// memory: N/A

/**
 * Return an array of arrays of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* assign_item(int* nums, int* indices, int numsSize){
    int i;
    int* item = (int*)malloc(sizeof(int) * numsSize);
    for(i = 0; i < numsSize; i ++){
        item[i] = nums[indices[i]];
        printf("%d, ", item[i]);
    }
    return item;
}

int** permute(int* nums, int numsSize, int* returnSize) {
    int size = numsSize;
    int** result = (int**)malloc(size * sizeof(int*));
    int* item = NULL;
    int indices[numsSize];
    int cycles[numsSize];
    int n = 0, i, j, tmp;
    
    // init indices
    // init cycles
    for(i = 0; i < numsSize; i ++){
        indices[i] = i;
        cycles[i] = numsSize - i;
    }
    
    item = assign_item(nums, indices, numsSize);
    result[n++] = item;
    
    while(numsSize){
        for(i = numsSize - 1; i >= 0; i --){
            cycles[i] -= 1;
            if(cycles[i] == 0){
                tmp = indices[i];
                for(j = i + 1; j < numsSize; j ++){
                    indices[j - 1] = indices[j];
                }
                indices[j - 1] = tmp;
                
                cycles[i] = numsSize - i;
            } else {
                j = cycles[i];
                tmp = indices[i];
                indices[i] = indices[numsSize - j];
                indices[numsSize - j] = tmp;
                item = assign_item(nums, indices, numsSize);
                result[n++] = item;
    
                if(n >= size){
                    size += 10;
                    result = (int**)realloc(result, size * sizeof(int*));
                }
                
                break;
            }
        }
        if(i < 0){
            *returnSize = n;
            return result;
        }
    }
    *returnSize = 0;
    return NULL;
}