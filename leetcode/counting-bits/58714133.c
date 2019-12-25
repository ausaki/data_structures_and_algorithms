// title: counting-bits
// detail: https://leetcode.com/submissions/detail/58714133/
// datetime: Mon Apr 11 13:01:32 2016
// runtime: 40 ms
// memory: N/A

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* retSize){
    int i, k, _2th, __2th;
    int* result = (int*)malloc(sizeof(int) * (num + 1));
    i = 0;
    result[0] = 0;
    _2th = 0x1 << i;
    while(_2th <= num){
        __2th = (0x1 << (i + 1));
        for(k = _2th; k < __2th && k <= num; k ++){
            result[k] = result[k - _2th] + 1;
        }
        if(k > num){
            break;
        }
        i ++; 
        _2th = __2th;
    
    }   
    *retSize = num + 1;
    return result;
}

