// title: permutation-sequence
// detail: https://leetcode.com/submissions/detail/145407234/
// datetime: Fri Mar 16 17:08:20 2018
// runtime: 40 ms
// memory: N/A

void nextPermutation(int* nums, int numsSize) {
    int i, j;
    int index1 = -1;
    int index2 = -1;
    int tmp;
    
    for(i = numsSize - 2; i >= 0; i --){
        if(nums[i] < nums[i + 1]){
            index1 = i;
            break;
        }
    }
    if(index1 == -1){
        for(i = 0, j = numsSize - 1; i < j; i++, j--){
            tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
        return ;
    }
    // 找到idnex的右边比nums[index]大且最接近的元素
    for(i = numsSize - 1; i > index1; i --){
        if(nums[i] > nums[index1]){
            index2 = i;
            break;
        }
    }
    // 替换index1 和 index2
    tmp = nums[index1];
    nums[index1] = nums[index2];
    nums[index2] = tmp;
    
    // 倒置index1 右边的元素
    for(i = index1 + 1, j = numsSize - 1; i < j; i++, j--){
        tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}

char* getPermutation(int n, int k) {
    int* nums = (int*)malloc(n * sizeof(int));
    int i = 0;
    char* result = (char*)malloc(n + 1);
        
    for(i = 0; i < n; i ++){
        nums[i] = i + 1;
    }
    for(i = 0; i < k - 1; i ++){
        nextPermutation(nums, n);
    }
    for(i = 0; i < n; i ++){
        result[i] = '0' + nums[i];
    }
    result[n] = 0;
    return result;
}