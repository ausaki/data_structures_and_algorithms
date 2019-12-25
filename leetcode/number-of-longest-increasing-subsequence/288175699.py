# title: number-of-longest-increasing-subsequence
# detail: https://leetcode.com/submissions/detail/288175699/
# datetime: Tue Dec 24 14:42:24 2019
# runtime: 820 ms
# memory: 12.7 MB

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        LIS = [None] * N
        for i in range(N):
            l, k = 0, 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if LIS[j][0] > l:
                        l, k = LIS[j]
                    elif LIS[j][0] == l:
                        k += LIS[j][1]
            l += 1
            LIS[i] = [l, k]
        res = 0
        l = 0
        for i, k in LIS:
            if i > l:
                l = i
                res = k
            elif i == l:
                res += k
        return res
