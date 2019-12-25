# title: longest-repeating-character-replacement
# detail: https://leetcode.com/submissions/detail/285802192/
# datetime: Sat Dec 14 10:44:48 2019
# runtime: 316 ms
# memory: 12.8 MB

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        if N == 0:
            return 0
        counter = dict.fromkeys(map(chr, range(ord('A'), ord('Z') + 1)), 0)
        left = 0
        right = 0
        counter[s[right]] += 1
        max_count = 1
        res = 0
        while right < N:
            print(left, right, max_count)
            if right - left + 1 - max_count <= k:
                right += 1
                if right >= N:
                    break
                counter[s[right]] += 1
                max_count = max(max_count, counter[s[right]])
            else:
                res = max(res, right - left)
                counter[s[left]] -= 1
                left += 1
                max_count = max(counter.values())
        res = max(res, right - left)
        return res
            
        
            
            
                