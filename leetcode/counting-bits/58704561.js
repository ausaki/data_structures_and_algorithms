// title: counting-bits
// detail: https://leetcode.com/submissions/detail/58704561/
// datetime: Mon Apr 11 11:08:39 2016
// runtime: 376 ms
// memory: N/A

/**
 * @param {number} num
 * @return {number[]}
 */
var countBits = function(num) {
    var result = new Array(num + 1);
    var i, k;
    for(i = 0; i < num + 1; i ++){
        result[i] = 0;
        for(k = 0; k < 32; k ++){
            if((i & (0x1 << k)) > 0){
                result[i] ++;
            }
        }
    }
    return result;
};