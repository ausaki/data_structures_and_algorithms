# title: matchsticks-to-square
# detail: https://leetcode.com/submissions/detail/286372804/
# datetime: Mon Dec 16 20:24:20 2019
# runtime: 460 ms
# memory: 66.7 MB

from functools import lru_cache
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def comb(a, b, c, d, i):
            if i == N:
                return a == q and b == q and c == q and d == q
            sides = [a, b, c, d]
            for j, s in enumerate(sides):
                if s + nums[i] <= q:
                    sides[j] += nums[i]
                    if comb(*sides, i + 1):
                        return True
                    sides[j] -= nums[i]
            return False
                                
        S = sum(nums)
        if S % 4: return False
        q = S // 4
        N = len(nums)
        if N <= 3: return False
        nums.sort(reverse=True)
        return comb(*[0, 0, 0, 0], 0)