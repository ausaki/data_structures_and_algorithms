# title: maximum-score-of-a-good-subarray
# detail: https://leetcode.com/submissions/detail/467490758/
# datetime: Sun Mar 14 11:35:21 2021
# runtime: 1412 ms
# memory: 25.3 MB

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        stack = []
        pos = [0] * n
        for i, j in enumerate(nums):
            while stack and j <= nums[stack[-1]]:
                stack.pop()
            pos[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        res = 0
        for i in range(n - 1, -1, -1):
            j = nums[i]
            while stack and  j <= nums[stack[-1]]:
                stack.pop()
            p = stack[-1] if stack else n
            stack.append(i)
            if p > k and pos[i] < k:
                res = max(res, j * (p - pos[i] - 1))
        return res
            
            