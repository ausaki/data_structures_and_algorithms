# title: product-of-array-except-self
# detail: https://leetcode.com/submissions/detail/284535872/
# datetime: Sun Dec  8 19:11:15 2019
# runtime: 128 ms
# memory: 19.4 MB

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        prev = 1
        back = 1
        for i in range(1, N):
            prev *= nums[i - 1]
            res[i] *= prev
            j = N - 1- i
            back *= nums[j + 1]
            res[j] *= back
        return res