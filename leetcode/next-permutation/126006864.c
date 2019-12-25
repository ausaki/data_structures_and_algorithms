// title: next-permutation
// detail: https://leetcode.com/submissions/detail/126006864/
// datetime: Mon Oct 30 21:48:41 2017
// runtime: 6 ms
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