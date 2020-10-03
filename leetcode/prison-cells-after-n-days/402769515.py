# title: prison-cells-after-n-days
# detail: https://leetcode.com/submissions/detail/402769515/
# datetime: Thu Oct  1 01:56:48 2020
# runtime: 40 ms
# memory: 14.1 MB

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        curr = 0
        for i, j in enumerate(cells):
            if j: curr |= j << i
        states = {curr: 0}        
        while N > 0:
            N -= 1
            new = 0
            for i in range(1, 7):
                if (curr >> (i - 1)) & 1 == (curr >> (i + 1)) & 1:
                    new |= 1 << i
            if new in states:
                i = states[new]
                j = states[curr]
                i = i + N % (j - i + 1)
                for k, v in states.items():
                    if v == i:
                        curr = k
                        break
                break
            else:
                curr = new
                states[curr] = len(states)
        return [(curr >> i) & 1 for i in range(8)]
