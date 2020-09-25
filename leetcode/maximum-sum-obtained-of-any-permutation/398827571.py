# title: maximum-sum-obtained-of-any-permutation
# detail: https://leetcode.com/submissions/detail/398827571/
# datetime: Tue Sep 22 01:50:00 2020
# runtime: 1392 ms
# memory: 46.4 MB

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        idx = [0] * (n + 1)
        for i, j in requests:
            idx[i] += 1
            idx[j + 1] -= 1
        for i in range(1, n):
            idx[i] += idx[i - 1]
        idx.pop()
        idx.sort()
        nums.sort()
        return sum(i * j for i, j in zip(idx, nums)) % (10 ** 9 + 7)