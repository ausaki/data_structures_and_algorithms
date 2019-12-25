# title: longest-repeating-character-replacement
# detail: https://leetcode.com/submissions/detail/285803035/
# datetime: Sat Dec 14 10:50:58 2019
# runtime: 264 ms
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
            if right - left + 1 - max_count <= k:
                right += 1
            else:
                res = max(res, right - left)
                char = ord(s[left]) - ord('A')
                counter[char] -= 1
                left += 1
                max_count = max(counter)
                right += 1
        res = max(res, right - left)
        return res
            
        
            
            
                