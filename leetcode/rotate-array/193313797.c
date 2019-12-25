// title: rotate-array
// detail: https://leetcode.com/submissions/detail/193313797/
// datetime: Tue Dec  4 18:41:21 2018
// runtime: 76 ms
// memory: 1.3 MB

void reverse(int* nums, int start, int end){
    int tmp;
    for(; start < end; start++, end--){
        tmp = nums[start];
        nums[start] = nums[end];
        nums[end] = tmp;
    }
}

void rotate(int* nums, int numsSize, int k) {
    int i, j, tmp;
    k = k % numsSize;
    if(k == numsSize){
        return;
    }
    reverse(nums, 0, numsSize - k - 1);
    for(i = 0; i < numsSize; i++){
        printf("%d, ", nums[i]);
    }
    printf("\n");
    reverse(nums, numsSize - k, numsSize - 1);
    for(i = 0; i < numsSize; i++){
        printf("%d, ", nums[i]);
    }
    printf("\n");
    reverse(nums, 0, numsSize - 1);
    for(i = 0; i < numsSize; i++){
        printf("%d, ", nums[i]);
    }
    printf("\n");
}