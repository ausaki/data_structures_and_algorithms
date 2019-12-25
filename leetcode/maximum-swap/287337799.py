# title: maximum-swap
# detail: https://leetcode.com/submissions/detail/287337799/
# datetime: Fri Dec 20 21:55:59 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        N = len(digits)
        for i in range(N):
            k = i
            for j in range(i + 1, N):
                if digits[j] >= digits[k]:
                    k = j
            if digits[k] > digits[i]:
                digits[i], digits[k] = digits[k], digits[i]
                return int(''.join(digits))
        return num