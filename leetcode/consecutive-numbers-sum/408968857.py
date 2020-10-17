# title: consecutive-numbers-sum
# detail: https://leetcode.com/submissions/detail/408968857/
# datetime: Thu Oct 15 15:09:14 2020
# runtime: 144 ms
# memory: 14.1 MB

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        result = 0
        for i in range(1, int(math.sqrt(2 * N)) + 1):
            q, r = divmod(2 * N, i)
            if r == 0 and q - i + 1 >= 2 and (q - i + 1) % 2 == 0:
                result += 1
        return result
                    