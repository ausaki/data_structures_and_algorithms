# title: word-break-ii
# detail: https://leetcode.com/submissions/detail/275819063/
# datetime: Mon Nov  4 13:09:12 2019
# runtime: 320 ms
# memory: 15.7 MB

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
        print(dp)
        result = []
        stack = [(N, '')]
        while stack:
            i, item = stack.pop()
            if i == 0:
                result.append(item.strip())
                continue
            for j, flag in enumerate(dp[i]):
                if flag > 0:
                    stack.append([i - len(wordDict[j]), wordDict[j] + ' ' + item])
                    
                    
        return result