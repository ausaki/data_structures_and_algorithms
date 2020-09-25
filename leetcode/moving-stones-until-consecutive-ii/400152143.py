# title: moving-stones-until-consecutive-ii
# detail: https://leetcode.com/submissions/detail/400152143/
# datetime: Thu Sep 24 22:59:45 2020
# runtime: 132 ms
# memory: 14.9 MB

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        max_ = max(stones[-1] - stones[1] + 1 - (n - 1), stones[-2] - stones[0] + 1 - (n - 1))
        i = 0
        min_ = n
        for j in range(n):
            while stones[j] - stones[i] + 1 > n:
                i += 1
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                min_ = min(min_, 2)
            else:
                min_ = min(min_, n - (j - i + 1))
            
        return [min_, max_]