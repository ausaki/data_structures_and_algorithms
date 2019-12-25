// title: counting-bits
// detail: https://leetcode.com/submissions/detail/58704632/
// datetime: Mon Apr 11 11:09:22 2016
// runtime: 64 ms
// memory: N/A

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize) {
    int i = 0, k = 0;
    int* result = (int*)malloc((num + 1) * sizeof(int));
    for(i = 0; i <= num; i ++){
        result[i] = 0;
        for(k = 0; k < sizeof(int) * 8; k++){
            if((i & (0x1 << k)) > 0){
                result[i] ++;
            }
        }
    }
    *returnSize = num + 1;
    return result;
}