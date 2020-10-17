# title: split-array-into-fibonacci-sequence
# detail: https://leetcode.com/submissions/detail/408530525/
# datetime: Wed Oct 14 13:57:16 2020
# runtime: 36 ms
# memory: 14 MB

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        digits = list(map(int, S))
        n = len(digits)
        M = (1 << 31) - 1
        def F(i, f):
            if i == n:
                return len(f) >= 3
            a, b = -1, -1
            if len(f) >= 2:
                a, b = f[-2], f[-1]
                if a > M - b:
                    return False
            c = a + b
            if digits[i] == 0:
                if len(f) < 2 or c == 0:
                    f.append(0)
                    if F(i + 1, f):
                        return True
                    f.pop()
                return False
            d = 0
            for j in range(i, min(i + 10, n)):
                if d <= (M - digits[j]) // 10:
                    d = d * 10 + digits[j]
                else:
                    break
                if len(f) < 2 or d == c:
                    f.append(d)
                    if F(j + 1, f):
                        return True
                    f.pop()
            return False
        f = []
        F(0, f)
        return f
                