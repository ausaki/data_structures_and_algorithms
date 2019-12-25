# title: longest-repeating-character-replacement
# detail: https://leetcode.com/submissions/detail/285804185/
# datetime: Sat Dec 14 10:59:48 2019
# runtime: 220 ms
# memory: 13 MB

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        if N == 0:
            return 0
        counter = [0] * 26
        left = 0
        right = 0
        max_count = 0
        res = 0
        while right < N:
            print(left, right, max_count)
            char = ord(s[right]) - ord('A')
            counter[char] += 1
            max_count = max(max_count, counter[char])
            while right - left + 1 - max_count > k:
                char = ord(s[left]) - ord('A')
                counter[char] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
            
        
            
            
# int len = s.length();
#         int[] count = new int[26];
#         int start = 0, maxCount = 0, maxLength = 0;
#         for (int end = 0; end < len; end++) {
#             maxCount = Math.max(maxCount, ++count[s.charAt(end) - 'A']);
#             while (end - start + 1 - maxCount > k) {
#                 count[s.charAt(start) - 'A']--;
#                 start++;
#             }
#             maxLength = Math.max(maxLength, end - start + 1);
#         }
#         return maxLength;