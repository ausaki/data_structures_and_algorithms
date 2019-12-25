# title: number-of-longest-increasing-subsequence
# detail: https://leetcode.com/submissions/detail/288179954/
# datetime: Tue Dec 24 15:04:58 2019
# runtime: 824 ms
# memory: 12.9 MB

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        LIS = [None] * N
        res = 0
        length = 0
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
            if l > length:
                length = l
                res = k
            elif l == length:
                res += k
        return res
