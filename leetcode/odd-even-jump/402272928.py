# title: odd-even-jump
# detail: https://leetcode.com/submissions/detail/402272928/
# datetime: Tue Sep 29 22:42:35 2020
# runtime: 272 ms
# memory: 18.5 MB

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        B = sorted(range(n), key=A.__getitem__)
        odds = [-1] * n 
        stack = []
        for i in B:
            while stack and i > stack[-1]:
                odds[stack.pop()] = i
            stack.append(i)
        evens = [-1] * n
        B = sorted(range(n), key=A.__getitem__, reverse=True)
        print(B)
        for i in B:
            while stack and i > stack[-1]:
                evens[stack.pop()] = i
            stack.append(i)
        dp = [[0, 0] for i in range(n)]
        dp[n - 1] = [1, 1]
        result = 1
        for i in range(n - 2, -1, -1):
            if odds[i] != -1 and dp[odds[i]][0]:
                dp[i][1] = 1
                result += 1
            if evens[i] != -1 and dp[evens[i]][1]:
                dp[i][0] = 1
        return result