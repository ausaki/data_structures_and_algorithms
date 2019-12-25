# title: longest-repeating-character-replacement
# detail: https://leetcode.com/submissions/detail/285806116/
# datetime: Sat Dec 14 11:13:33 2019
# runtime: 76 ms
# memory: 12.9 MB

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        counter = collections.defaultdict(int)
        left = 0
        right = 0
        max_count = 0
        max_char = 'x'
        res = 0
        while right < N:
            counter[s[right]] += 1
            if counter[s[right]] > max_count:
                max_count = counter[s[right]]
                max_char = s[right]
            if right - left + 1 - max_count > k:
                counter[s[left]] -= 1
                if s[left] == max_char:
                    max_count -= 1
                left += 1
            right += 1
        return right - left
            
        
            
            
