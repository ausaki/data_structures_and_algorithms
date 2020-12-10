# title: find-the-most-competitive-subsequence
# detail: https://leetcode.com/submissions/detail/425238894/
# datetime: Sun Nov 29 12:35:22 2020
# runtime: 1512 ms
# memory: 27.6 MB

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == k:
            return nums
        stack = []
        for i, num in enumerate(nums):
            while stack and num < stack[-1]:
                if len(stack) + n - i - 1 >= k:
                    stack.pop()
                else:
                    break
            if len(stack) < k:
                stack.append(num)
            
        return stack