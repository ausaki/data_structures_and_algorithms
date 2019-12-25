// title: house-robber
// detail: https://leetcode.com/submissions/detail/193497001/
// datetime: Wed Dec  5 17:57:12 2018
// runtime: 0 ms
// memory: N/A

int rob_(int* nums, int s, int numsSize, int* cache) {
    int result1 = 0,
        result2 = 0;
    if(numsSize - s <= 0){
        return 0;
    }
    if(numsSize - s == 1){
        return nums[s] ;
    }
    if(cache[s] >= 0){
        return cache[s];
    }
    result1 = nums[s] + rob_(nums, s + 2, numsSize, cache);
    result2 = nums[s + 1] + rob_(nums, s + 3, numsSize, cache);
    cache[s] = result1 > result2 ? result1 : result2;
    return cache[s];
}

int rob(int* nums, int numsSize) {
    int* cache = (int*)malloc(sizeof(int) * numsSize);
    for(int i = 0; i < numsSize; i++){
        cache[i] = -1;
    }
    return rob_(nums, 0, numsSize, cache);
}