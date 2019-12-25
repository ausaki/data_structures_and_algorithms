// title: total-hamming-distance
// detail: https://leetcode.com/submissions/detail/280091581/
// datetime: Tue Nov 19 19:11:29 2019
// runtime: 68 ms
// memory: 8 MB



int totalHammingDistance(int* nums, int numsSize){
    int bucket[31];
    int i, j, total = 0;
    for(j = 0; j < 31; j++){
        bucket[j] = 0;
    }
    for(i = 0; i < numsSize; i++){
        for(j = 0; j < 31; j++){
            if((1 << j) & nums[i]){
                bucket[j] ++;
            }
        }
    } 
    for(j = 0; j < 31; j++){
        if(bucket[j] > 0){
            total += bucket[j] * (numsSize - bucket[j]);
        }
    }
    return total;
}

