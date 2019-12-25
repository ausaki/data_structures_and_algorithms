// title: majority-element
// detail: https://leetcode.com/submissions/detail/193280741/
// datetime: Tue Dec  4 14:41:30 2018
// runtime: 1708 ms
// memory: N/A

int quicksort(int* nums, int start, int end){
    if(start >= end){
        return -1;
    }
    int i = 0,
        h = start, 
        tmp = 0,
        pivot = nums[start];
    
    for(i = h + 1; i <= end; i++){
        if(nums[i] <= pivot){
            h++;
            tmp = nums[h];
            nums[h] = nums[i];
            nums[i] = tmp;
        }
    }
    tmp = nums[h];
    nums[h] = pivot;
    nums[start] = tmp;
    quicksort(nums, start, h - 1);
    quicksort(nums, h + 1, end);
    return 0;
}


int majorityElement(int* nums, int numsSize) {
    int i,
        n,
        c,
        times = numsSize / 2;
    quicksort(nums, 0, numsSize - 1);
    return nums[times];
}