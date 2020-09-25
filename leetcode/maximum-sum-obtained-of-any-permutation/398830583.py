# title: maximum-sum-obtained-of-any-permutation
# detail: https://leetcode.com/submissions/detail/398830583/
# datetime: Tue Sep 22 01:58:34 2020
# runtime: 1408 ms
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
        idx.sort(reverse=True)
        nums.sort(reverse=True)
        s = 0
        MOD = 10 ** 9 + 7
        for i in range(n):
            if idx[i] == 0:
                break
            s = (s + nums[i] * idx[i]) % MOD
        return s