# title: next-greater-element-ii
# detail: https://leetcode.com/submissions/detail/282271345/
# datetime: Thu Nov 28 21:04:07 2019
# runtime: 228 ms
# memory: 14.7 MB

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [-1] * N
        stack = []
        for i in range(N):
            while stack and nums[i] > stack[-1][0]:
                n, j = stack.pop()
                res[j] = nums[i]
            stack.append([nums[i], i])
        if len(stack) > 1:
            for i in range(stack[0][1] + 1):
                while len(stack) > 1 and nums[i] > stack[-1][0]:
                    n, j = stack.pop()
                    res[j] = nums[i]
                stack.append([nums[i], i])
        return res