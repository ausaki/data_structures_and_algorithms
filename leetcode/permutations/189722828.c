// title: permutations
// detail: https://leetcode.com/submissions/detail/189722828/
// datetime: Thu Nov 15 18:09:01 2018
// runtime: 4 ms
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

int** permute_py(int* nums, int numsSize, int* returnSize) {
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

int** permute_recursive(int* nums, int numsSize, int* returnSize){
    *returnSize = 0;
    if(numsSize == 0){
        return NULL;
    }
    int i = 0, j = 0, k = 0;
    int* item = NULL;
    int size = 10;
    int** parts = NULL;
    int** result = (int**)malloc(size * sizeof(int*));
    if(numsSize == 1){
        item = (int*)malloc(1 * sizeof(int));
        item[0] = nums[0];
        result[(*returnSize)++] = item;
        return result;
    }
    // nums = sorted(nums)
    // if(numsSize == 2){
    //     item = (int*)malloc(2 * sizeof(int));
    //     item[0] = nums[0];
    //     item[1] = nums[1];
    //     result[(*returnSize)++] = item;
    //     item = (int*)malloc(2 * sizeof(int));
    //     item[0] = nums[1];
    //     item[1] = nums[0];
    //     result[(*returnSize)++] = item;
    //     return result;
    // }
    parts = permute_recursive(nums + 1, numsSize - 1, returnSize);
    for(i = 0; i < *returnSize; i ++){
        for(j = 0; j < numsSize; j ++){
            item = (int*)malloc(numsSize * sizeof(int));
            for(k = 0; k < numsSize; k ++){
                if(k < j){
                    item[k] = parts[i][k];
                } else if(k == j){
                    item[k] = nums[0];
                } else {
                    item[k] = parts[i][k - 1];
                }
            }
            if(i * numsSize + j >= size){
                size *= 2;
                result = (int**)realloc(result, size * sizeof(int*));
            }
            result[i * numsSize + j] = item;
        }
    }
    *returnSize = numsSize * (*returnSize);
    return result;
}


int** permute(int* nums, int numsSize, int* returnSize) {
    int** result = permute_recursive(nums, numsSize, returnSize);
    return result;
}


// int fact(int n){
//     if(n==1)return 1;
//     return n*fact(n-1);
// }
// int idx;
// int **a;
// void util(int start,int n,int arr[n]){
//     int i,j,tmp;
//     if(start==n){
//         for(i=0;i<n;i++){
//             a[idx][i]=arr[i];
//         }
//         idx++;
//         return;
//     }
//     for(i=start;i<n;i++){
//         tmp=arr[i];
//         arr[i]=arr[start];
//         arr[start]=tmp;
//         util(start+1,n,arr);
//         tmp=arr[i];
//         arr[i]=arr[start];
//         arr[start]=tmp;
//     }
// }
// int** permute(int* nums, int n, int* returnSize) {
//     int i,j,k,total=fact(n),arr[n];
//     a=(int *)malloc(total*sizeof(int*));
//     for(i=0;i<total;i++){
//         a[i]=(int *)malloc(n*sizeof(int));
//     }
//     printf("%d",total);
//     idx=0;
//     for(i=0;i<n;i++){
//         arr[i]=nums[i];
//     }
//     util(0,n,arr);
//     *returnSize=total;
//     return a;
// }