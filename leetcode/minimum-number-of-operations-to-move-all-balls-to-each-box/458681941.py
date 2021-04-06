# title: minimum-number-of-operations-to-move-all-balls-to-each-box
# detail: https://leetcode.com/submissions/detail/458681941/
# datetime: Sun Feb 21 13:16:30 2021
# runtime: 60 ms
# memory: 14.6 MB

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        cnt, ops = 0, 0
        for i in range(n):
            if boxes[i] == '1':
                cnt += 1
                ops += i
        cnt2, ops2 = 0, 0
        for i in range(n):
            res[i] = ops + ops2
            if boxes[i] == '1':
                cnt2 += 1
                cnt -= 1
            ops2 += cnt2
            ops -= cnt
        return res