# title: find-the-most-competitive-subsequence
# detail: https://leetcode.com/submissions/detail/425239485/
# datetime: Sun Nov 29 12:37:11 2020
# runtime: 1572 ms
# memory: 27.5 MB

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == k:
            return nums
        stack = []
        for i, num in enumerate(nums):
            while stack and num < stack[-1] and len(stack) + n - i - 1 >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack