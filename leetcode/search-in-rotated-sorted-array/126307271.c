// title: search-in-rotated-sorted-array
// detail: https://leetcode.com/submissions/detail/126307271/
// datetime: Wed Nov  1 19:19:46 2017
// runtime: 6 ms
// memory: N/A

int bi_search(int* nums, int start, int end, int target){
    int i, j, m;
    printf("start = %d, end=%d\n", start, end);
    if(start > end){
        return -1;
    }
    m = (start + end) / 2;
    if(nums[m] == target){
        return m;
    }
    if(nums[m] < target){
        return bi_search(nums, m + 1, end, target);
    }
    return bi_search(nums, start, m - 1, target);
}

int search(int* nums, int numsSize, int target) {
    // 1. 找到次序颠倒的那个元素索引
    // 2. 一次对前后两个递增序列进行二分查找
    int i, j;
    int index = -1;
    for(i = 0, j = numsSize - 1; i < j; i ++, j --){
        if(nums[i] > nums[i + 1]){
            index = i + 1;
            break;
        }
        if(nums[j] < nums[j - 1]){
            index = j;
            break;
        }
    }
    printf("index = %d\n", index);
    if(index == -1){
        printf("-1\n");
        return bi_search(nums, 0, numsSize - 1, target);
    }
    i = bi_search(nums, 0, index - 1, target);
    if(i != -1){
        return i;
    }
    return bi_search(nums, index, numsSize - 1, target);
}