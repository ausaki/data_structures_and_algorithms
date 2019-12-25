// title: remove-element
// detail: https://leetcode.com/submissions/detail/125570627/
// datetime: Fri Oct 27 18:33:36 2017
// runtime: 3 ms
// memory: N/A

int removeElement(int* nums, int numsSize, int val) {
    int num;
    int i;
    int count = 0;
    
    for(i = 0; i < numsSize; i ++){
        if(nums[i] != val){
            nums[count] = nums[i];
            count ++;
        }
    }
    return count;
}