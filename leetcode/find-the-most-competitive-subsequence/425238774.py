# title: find-the-most-competitive-subsequence
# detail: https://leetcode.com/submissions/detail/425238774/
# datetime: Sun Nov 29 12:34:59 2020
# runtime: 1260 ms
# memory: 27.2 MB

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
            
        return stack[:k]