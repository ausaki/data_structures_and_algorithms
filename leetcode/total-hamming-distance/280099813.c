// title: total-hamming-distance
// detail: https://leetcode.com/submissions/detail/280099813/
// datetime: Tue Nov 19 20:37:17 2019
// runtime: 48 ms
// memory: 7.9 MB



int totalHammingDistance(int* nums, int numsSize){
    int i, j, count, total = 0;
    for(j = 0; j < 31; j++){
        count = 0;
        for(i = 0; i < numsSize; i++){
            count += nums[i] & 1;
            nums[i] >>= 1;
        }
        total += count * (numsSize - count);
    }
    return total;
}

