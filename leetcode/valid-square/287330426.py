# title: valid-square
# detail: https://leetcode.com/submissions/detail/287330426/
# datetime: Fri Dec 20 20:35:20 2019
# runtime: 32 ms
# memory: 12.7 MB

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        '''
        2  ______ 4
          |      |
          |      |
        1 |______| 3
        
        '''
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        d1 = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        d2 = (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2
        d3 = (p4[0] - p2[0]) ** 2 + (p4[1] - p2[1]) ** 2
        d4 = (p4[0] - p3[0]) ** 2 + (p4[1] - p3[1]) ** 2
        d5 = (p4[0] - p1[0]) ** 2 + (p4[1] - p1[1]) ** 2
        return d1 == d2 == d3 == d4 != 0 and d5 == d1 + d2
