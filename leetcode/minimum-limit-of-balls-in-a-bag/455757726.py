# title: minimum-limit-of-balls-in-a-bag
# detail: https://leetcode.com/submissions/detail/455757726/
# datetime: Sun Feb 14 11:02:35 2021
# runtime: 2544 ms
# memory: 27.1 MB

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(m):
            ops = 0
            for i in reversed(nums):
                if i <= m:
                    break
                q, r = divmod(i, m)
                ops += q - 1 + (r > 0)
            return ops <= maxOperations
        
        nums.sort()
        l, r = 1, nums[-1]
        while l <= r:
            m = (l + r) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l