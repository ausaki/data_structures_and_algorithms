# title: minimum-difficulty-of-a-job-schedule
# detail: https://leetcode.com/submissions/detail/390884278/
# datetime: Fri Sep  4 18:14:49 2020
# runtime: 48 ms
# memory: 13.9 MB

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if N<d: return -1
        
        dp = [jobDifficulty[0]]
        for j in jobDifficulty[1:]:
            dp.append(max(dp[-1], j))

        for i in range(1, d):
            stack = []
            dp2 = [0]*N
            for j in range(i, N):
                dp2[j] = dp[j-1]+jobDifficulty[j]
                while stack and jobDifficulty[stack[-1]]<=jobDifficulty[j]:
                    dp2[j] = min(dp2[j], dp2[stack[-1]]-jobDifficulty[stack[-1]]+jobDifficulty[j])
                    # dp2[j] = min(dp2[j], dp[stack[-1]]+jobDifficulty[j])
                    stack.pop()
                    
                if stack:
                    dp2[j] = min(dp2[j], dp2[stack[-1]])
                    
                stack.append(j)
            dp = dp2
            # print(dp)
        return dp[-1]