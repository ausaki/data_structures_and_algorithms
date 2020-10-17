# title: flipping-an-image
# detail: https://leetcode.com/submissions/detail/408668684/
# datetime: Wed Oct 14 23:14:59 2020
# runtime: 52 ms
# memory: 14.1 MB

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[(i + 1) % 2 for i in reversed(row)] for row in A]
