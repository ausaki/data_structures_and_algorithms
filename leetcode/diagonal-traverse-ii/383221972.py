# title: diagonal-traverse-ii
# detail: https://leetcode.com/submissions/detail/383221972/
# datetime: Wed Aug 19 22:03:32 2020
# runtime: 1096 ms
# memory: 78.3 MB

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = []
        n = len(nums)
        for i in range(n):
            for j, num in enumerate(nums[i]):
                c = i + j
                if c == len(diagonals):
                    diagonals.append(collections.deque())
                diagonals[c].appendleft(num)
        result = []
        for a in diagonals:
            result.extend(a)
        return result