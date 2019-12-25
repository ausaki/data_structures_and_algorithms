// title: permutations-ii
// detail: https://leetcode.com/submissions/detail/189900925/
// datetime: Fri Nov 16 15:45:12 2018
// runtime: 8 ms
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
    }
    return item;
}

int comp(void *a, void *b){
    return *((int*)a) - *((int*)b);
}
int** permuteUnique(int* nums, int numsSize, int* returnSize) {
    if(numsSize == 0){
        *returnSize = 0;
        return NULL;
    }
    
    qsort(nums, numsSize, sizeof(int), comp);
    
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
        cycles[i] = i;
    }
    
    item = assign_item(nums, indices, numsSize);
    result[(*returnSize)++] = item;
    
    while(1){
        for(i = numsSize - 1; i >= 0; i --){
            cycles[i] += 1;
            if(cycles[i] == numsSize){
                tmp = indices[i];
                for(j = i + 1; j < numsSize; j ++){
                    indices[j - 1] = indices[j];
                }
                indices[j - 1] = tmp;
                cycles[i] = i;
            } else {
                j = cycles[i];
                while(j < numsSize && nums[indices[i]] == nums[indices[j]]){
                    j ++;
                }
                if(j < numsSize){
                    cycles[i] = j;
                    tmp = indices[i];
                    indices[i] = indices[j];
                    indices[j] = tmp;
                    item = assign_item(nums, indices, numsSize);
                    if(*returnSize >= size){
                        size += 10;
                        result = (int**)realloc(result, size * sizeof(int*));
                    }
                    result[(*returnSize)++] = item;
                    break;
                } else {
                    tmp = indices[i];
                    for(j = i + 1; j < numsSize; j ++){
                        indices[j - 1] = indices[j];
                    }
                    indices[j - 1] = tmp;
                    cycles[i] = i;
                }
            }
        }
        if(i < 0){
            return result;
        }
    }
}