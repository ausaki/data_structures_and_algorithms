# title: word-break
# detail: https://leetcode.com/submissions/detail/275601721/
# datetime: Sun Nov  3 23:02:50 2019
# runtime: 44 ms
# memory: 14 MB

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # self.cache = [-1] * len(s)
        # return self._break(s, 0, wordDict)
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        for i in range(1, len(s) + 1):
            for w in wordDict:
                prev = i - len(w)
                if prev < 0:
                    continue
                if (dp[prev] > 0) and s[prev:i] == w:
                    dp[i] = 1
        return dp[-1] > 0
                    
    def _break(self, s, start, wordDict):
        if start == len(s):
            return True
        if self.cache[start] >= 0:
            return self.cache[start] > 0
        
        for w in wordDict:
            if len(w) > len(s) - start:
                continue
            for i in range(len(w)):
                if s[start + i] != w[i]:
                    break
            else:
                res = self._break(s, start + len(w), wordDict)
                if res:
                    self.cache[start] = 1
                    return True
        self.cache[start] = 0
        return False
    
    
        