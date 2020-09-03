# title: daily-temperatures
# detail: https://leetcode.com/submissions/detail/290045987/
# datetime: Tue Dec 31 23:38:14 2019
# runtime: 504 ms
# memory: 16.6 MB

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        N = len(T)
        stack = [0]
        res = [0] * N
        for i in range(1, N):
            while stack and T[i] > T[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
                