# title: minimum-operations-to-reduce-x-to-zero
# detail: https://leetcode.com/submissions/detail/420801204/
# datetime: Mon Nov 16 15:19:27 2020
# runtime: 1216 ms
# memory: 36.7 MB

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        t = sum(nums) - x
        if t == 0:
            return n
        prefix = {0: -1}
        s = 0
        ans = n
        for i, j in enumerate(nums):
            s += j
            k = prefix.get(s - t, n)
            ans = min(ans, n - i + k)
            prefix[s] = i
        return ans if ans < n else -1