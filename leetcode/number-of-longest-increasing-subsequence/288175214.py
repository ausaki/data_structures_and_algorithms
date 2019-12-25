# title: number-of-longest-increasing-subsequence
# detail: https://leetcode.com/submissions/detail/288175214/
# datetime: Tue Dec 24 14:39:52 2019
# runtime: 852 ms
# memory: 12.8 MB

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        LIS = [None] * N
        for i in range(N):
            l = [0, 1]
            for j in range(i):
                if nums[i] > nums[j]:
                    if LIS[j][0] > l[0]:
                        l = LIS[j][:]
                    elif LIS[j][0] == l[0]:
                        l[1] += LIS[j][1]
            l[0] += 1
            LIS[i] = l
        res = 0
        l = 0
        for i, k in LIS:
            if i > l:
                l = i
                res = k
            elif i == l:
                res += k
        return res
