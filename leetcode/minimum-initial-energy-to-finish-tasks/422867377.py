# title: minimum-initial-energy-to-finish-tasks
# detail: https://leetcode.com/submissions/detail/422867377/
# datetime: Sun Nov 22 14:20:04 2020
# runtime: 1260 ms
# memory: 59.4 MB

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        '''
        假设T是tasks列表的最优排列，初始energy等于E，最后剩余的energy等于L，
        题目转化为找到T和L使得E最小。
        
        从后往前推导：
        第n步，E[n] = L
        第n - 1步，E[n - 1] = max(E[n] + T[n - 1][0], T[n - 1][1])
        第n - 2步，E[n - 2] = max(E[n - 1] + T[n - 2][0], T[n - 2][1])
        ...
        第0步, E[0] = max(E[1] + T[0][0], E[0] >= T[0][1])
        
        递推公式: E[n] = max(E[n + 1] + T[n][0], E[n] >= T[n][1])
        
        假设只有一个task, 那么E[0]等于T[0][1], E[1] = T[0][1] - T[0][0].
        
        
        '''
        tasks.sort(key=lambda p: p[1] - p[0])
        e = 0
        for a, m in tasks:
            e = max(e + a, m)
        return e