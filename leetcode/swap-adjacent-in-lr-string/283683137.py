# title: swap-adjacent-in-lr-string
# detail: https://leetcode.com/submissions/detail/283683137/
# datetime: Wed Dec  4 22:05:34 2019
# runtime: 40 ms
# memory: 12.8 MB

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        S = len(start)
        E = len(end)
        if S != E:
            return False
        i = 0
        start = list(start)
        end = list(end)
        while i < S:
            if start[i] == end[i]:
                i += 1
            else:
                if start[i] == 'X' and end[i] == 'L':
                    k = i + 1
                    while k < S and start[k] == 'X':
                        k += 1
                    if k < S and start[k] == 'L':
                        start[i], start[k] = start[k], start[i]
                        i += 1
                    else:
                        return False
                elif start[i] == 'R' and end[i] == 'X':
                    k = i + 1
                    while k < S and start[k] == 'R':
                        k += 1
                    if k < S and start[k] == 'X':
                        start[i], start[k] = start[k], start[i]
                        i += 1
                    else:
                        return False
                else:
                    return False
        return True