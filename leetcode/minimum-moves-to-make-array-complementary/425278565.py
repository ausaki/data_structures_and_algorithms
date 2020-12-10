# title: minimum-moves-to-make-array-complementary
# detail: https://leetcode.com/submissions/detail/425278565/
# datetime: Sun Nov 29 14:55:27 2020
# runtime: 1252 ms
# memory: 29.1 MB

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        delta = [0] * (2 * limit + 2)
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1
            
        curr = 0            
        res = math.inf
        for i in range(2, 2 * limit + 1):
            curr += delta[i]
            res = min(res, curr)
        return res   