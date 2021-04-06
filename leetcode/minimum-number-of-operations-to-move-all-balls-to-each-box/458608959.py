# title: minimum-number-of-operations-to-move-all-balls-to-each-box
# detail: https://leetcode.com/submissions/detail/458608959/
# datetime: Sun Feb 21 10:40:04 2021
# runtime: 8128 ms
# memory: 14.7 MB

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        for i in range(n):
            for j in range(n):
                if boxes[j] == '1':
                    res[i] += abs(i - j)
        return res