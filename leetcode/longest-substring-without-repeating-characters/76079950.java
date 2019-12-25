// title: longest-substring-without-repeating-characters
// detail: https://leetcode.com/submissions/detail/76079950/
// datetime: Tue Sep 27 21:21:42 2016
// runtime: 45 ms
// memory: N/A

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        int[] index = new int[128]; // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            i = Math.max(index[s.charAt(j)], i);
            ans = Math.max(ans, j - i + 1);
            index[s.charAt(j)] = j + 1;
        }
        return ans;
    }
}