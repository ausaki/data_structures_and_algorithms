# title: longest-repeating-character-replacement
# detail: https://leetcode.com/submissions/detail/285802571/
# datetime: Sat Dec 14 10:47:37 2019
# runtime: 276 ms
# memory: 13 MB

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        if N == 0:
            return 0
        counter = dict.fromkeys(map(chr, range(ord('A'), ord('Z') + 1)), 0)
        left = 0
        right = 0
        max_count = 0
        res = 0
        while right < N:
            print(left, right, max_count)
            counter[s[right]] += 1
            max_count = max(max_count, counter[s[right]])
            if right - left + 1 - max_count <= k:
                right += 1
            else:
                res = max(res, right - left)
                counter[s[left]] -= 1
                left += 1
                max_count = max(counter.values())
                right += 1
        res = max(res, right - left)
        return res
            
        
            
            
                