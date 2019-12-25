// title: counting-bits
// detail: https://leetcode.com/submissions/detail/58704657/
// datetime: Mon Apr 11 11:09:36 2016
// runtime: 19 ms
// memory: N/A

public class Solution {
    public int[] countBits(int num) {
        int[] result = new int[num + 1];
        int i, k;
        for(i = 0; i < num + 1; i ++){
            result[i] = 0;
            for(k = 0; k < 32; k ++){
                if((i & (0x1 << k)) > 0){
                    result[i] ++;
                }
            }
        }
        return result;
    }
}