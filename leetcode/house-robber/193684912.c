// title: house-robber
// detail: https://leetcode.com/submissions/detail/193684912/
// datetime: Thu Dec  6 18:46:35 2018
// runtime: 0 ms
// memory: 1.1 MB

#define max(a, b) ((a) > (b) ? (a) : (b))

int rob(int* nums, int numsSize) {
    int a = 0, b = 0, i = 0, tmp;
    for(int i = 0; i < numsSize; i++){
        tmp = b;
        b = max(b, nums[i] + a);
        a = tmp;
    }
    return b;
}