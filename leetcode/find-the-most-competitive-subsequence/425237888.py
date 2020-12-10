# title: find-the-most-competitive-subsequence
# detail: https://leetcode.com/submissions/detail/425237888/
# datetime: Sun Nov 29 12:32:03 2020
# runtime: 1240 ms
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
            stack.append(num)
            
        return stack[:k]