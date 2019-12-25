# title: matchsticks-to-square
# detail: https://leetcode.com/submissions/detail/286372957/
# datetime: Mon Dec 16 20:25:42 2019
# runtime: 1652 ms
# memory: 12.7 MB

from functools import lru_cache
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        def comb(sides, i):
            if i == N:
                return all(s == q for s in sides)
            for j, s in enumerate(sides):
                if s + nums[i] <= q:
                    sides[j] += nums[i]
                    if comb(sides, i + 1):
                        return True
                    sides[j] -= nums[i]
            return False
                                
        S = sum(nums)
        if S % 4: return False
        q = S // 4
        N = len(nums)
        if N <= 3: return False
        nums.sort(reverse=True)
        return comb([0, 0, 0, 0], 0)