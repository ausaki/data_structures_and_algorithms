# title: find-the-most-competitive-subsequence
# detail: https://leetcode.com/submissions/detail/425236171/
# datetime: Sun Nov 29 12:26:52 2020
# runtime: 1532 ms
# memory: 27.3 MB

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == k:
            return nums
        stack = []
        for i, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                if len(stack) + n - i - 1 >= k:
                    stack.pop()
                else:
                    break
            stack.append(i)
        return [nums[stack[i]] for i in range(k)]