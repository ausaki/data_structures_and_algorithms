// title: maximum-product-of-two-elements-in-an-array
// detail: https://leetcode.com/submissions/detail/381248508/
// datetime: Sat Aug 15 23:03:05 2020
// runtime: 4 ms
// memory: 5.7 MB



int maxProduct(int* nums, int numsSize){
    int a = nums[0], b = nums[1];
    if(a > b){
        a ^= b;
        b ^= a;
        a ^= b;
    }
    for(int i = 2; i < numsSize; i++){
        if(nums[i] <= a)
            continue;
        if(nums[i] <= b){
            a = nums[i];
        } else{
            a = b;
            b = nums[i];
        }
    }
    return (a - 1) * (b - 1);
}