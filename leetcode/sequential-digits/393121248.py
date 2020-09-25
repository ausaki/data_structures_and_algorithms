# title: sequential-digits
# detail: https://leetcode.com/submissions/detail/393121248/
# datetime: Wed Sep  9 12:43:39 2020
# runtime: 20 ms
# memory: 14 MB

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        t = [12, 23, 34, 45, 56, 67, 78, 89]
        result = []
        while t:
            for i, j in enumerate(t):
                if low <= j <= high:
                    result.append(j)
                if j > high:
                    break
                k = j % 10 + 1
                if k <= 9:
                    t[i] = j * 10 + k
                else:
                    t.pop()
            else:
                continue
            break
        return result