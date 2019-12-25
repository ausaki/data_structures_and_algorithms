// title: remove-duplicates-from-sorted-array
// detail: https://leetcode.com/submissions/detail/125570418/
// datetime: Fri Oct 27 18:27:32 2017
// runtime: 12 ms
// memory: N/A

int removeDuplicates(int* nums, int numsSize) {
    int num = 0;
    int count = 0;
    int tmp_val = 0;
    int i = 0;
    
    if(numsSize == 0){
        return 0;
    }
    num = nums[0];
    count = 1;
    for(i = 1; i < numsSize; i ++){
        if(nums[i] != num){
            num = nums[i];
            nums[count] = num;
            count ++;
        }
    }
    return count;
}