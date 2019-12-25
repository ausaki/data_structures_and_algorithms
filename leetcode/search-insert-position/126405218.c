// title: search-insert-position
// detail: https://leetcode.com/submissions/detail/126405218/
// datetime: Thu Nov  2 10:57:08 2017
// runtime: 3 ms
// memory: N/A

int searchInsert(int* nums, int numsSize, int target) {
    int start, end, m, index;
    start = 0;
    end = numsSize - 1;
    
    index = -1;
    
    while(start <= end){
        m = (start + end) / 2;
        if(nums[m] == target){
            index = m;
            break;
        }
        if(nums[m] < target){
            start = m + 1;
        } else {
            end = m - 1;
        }
        
    }
    if(index != -1){
        return index;
    }
    if(nums[m] < target){
        index = m + 1;
    } else {
        index = m;
    }
    return index;
}