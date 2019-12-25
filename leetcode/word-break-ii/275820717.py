# title: word-break-ii
# detail: https://leetcode.com/submissions/detail/275820717/
# datetime: Mon Nov  4 13:15:06 2019
# runtime: 332 ms
# memory: 14.6 MB

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        dp = [[0 for _ in range(len(wordDict))] for _ in range(N + 1)] 
        for i in range(len(wordDict)):
            dp[0][i] = 1
        
        for i in range(1, N + 1):
            for j, w in enumerate(wordDict):
                prev = i - len(w)
                if prev < 0:
                    continue
                if any(dp[prev]) and s[prev:i] == w:
                    dp[i][j] = 1
        self.result = []
        self.wordDict = wordDict
        self._traverse(dp, N, '')
        return self.result
    
    def _traverse(self, dp, i, item):
        if i == 0:
            self.result.append(item.strip())
            return
        for j, flag in enumerate(dp[i]):
            if flag > 0:
                self._traverse(dp, i - len(self.wordDict[j]), self.wordDict[j] + ' ' + item)
    