# title: diagonal-traverse-ii
# detail: https://leetcode.com/submissions/detail/383230063/
# datetime: Wed Aug 19 22:25:46 2020
# runtime: 1012 ms
# memory: 33.5 MB

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = []
        n = len(nums)
        a = [(i + j, j, k)  for i, row in enumerate(nums) for j, k in enumerate(row)]
        a.sort()
        return [item[2] for item in a]