# title: number-of-rectangles-that-can-form-the-largest-square
# detail: https://leetcode.com/submissions/detail/443905883/
# datetime: Sun Jan 17 10:33:02 2021
# runtime: 232 ms
# memory: 15 MB

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_l = 0
        res = 0
        for l, w in rectangles:
            m = min(l, w)
            if m > max_l:
                max_l = m
                res = 1
            elif m == max_l:
                res += 1
            
        return res