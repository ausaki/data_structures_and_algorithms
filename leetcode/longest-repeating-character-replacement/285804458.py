# title: longest-repeating-character-replacement
# detail: https://leetcode.com/submissions/detail/285804458/
# datetime: Sat Dec 14 11:01:38 2019
# runtime: 76 ms
# memory: 12.8 MB

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s):
            return len(s)
        
        left, maxC = 0, 0
        ch = ''
        dic = collections.defaultdict(int)
        
        for i in range(len(s)):
            dic[s[i]] += 1
            
            if dic[s[i]] > maxC:
                maxC = dic[s[i]]
                ch = s[i]
            
            if i-left+1-maxC > k:
                dic[s[left]] -= 1
                if s[left] == ch:
                    maxC -= 1
                left += 1
        
        return i-left+1