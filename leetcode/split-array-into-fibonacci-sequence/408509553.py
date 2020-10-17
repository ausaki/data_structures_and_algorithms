# title: split-array-into-fibonacci-sequence
# detail: https://leetcode.com/submissions/detail/408509553/
# datetime: Wed Oct 14 12:58:01 2020
# runtime: 36 ms
# memory: 13.9 MB

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        digits = list(map(int, S))
        n = len(digits)
        M = (1 << 31) - 1
        def F(i, f):
            if i == n:
                return True
            a, b = f[-2], f[-1]
            if a > M - b:
                return False
            c = a + b
            d = 0
            if digits[i] == 0:
                if c == 0:
                    f.append(0)
                    return F(i + 1, f)
                return False
            for j in range(i, min(i + 10, n)):
                d * 10 + digits[j] <= M
                if d <= (M - digits[j]) // 10:
                    d = d * 10 + digits[j]
                else:
                    break
                if d == c:
                    f.append(c)
                    return F(j + 1, f)
            return False
        a = 0
        for i in range(min(10, n)):
            if a > (M - digits[i]) // 10:
                break
            a = a * 10 + digits[i]
            b = 0
            for j in range(i + 1, min(i + 11, n)):
                if b > (M - digits[j]) // 10:
                    break
                b = b * 10 + digits[j]
                f = [a, b]
                if j + 1 < n and F(j + 1, f):
                    return f
                if j == i + 1 and digits[j] == 0:
                    break
            if i == 0 and digits[i] == 0:
                break
        return []
                