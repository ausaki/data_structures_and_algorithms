# title: numbers-at-most-n-given-digit-set
# detail: https://leetcode.com/submissions/detail/405233919/
# datetime: Tue Oct  6 19:19:30 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_digits = str(n)
        t = len(digits)
        m = len(n_digits)
        total = 0
        for i in range(1, m):
            total += pow(t, i)
        print(total)
        for i, d in enumerate(n_digits):
            l = sum(1 for j in digits if j < d)
            if l:
                total += l * pow(t, (m - i - 1))
            if d not in digits:
                break
        else:
            total += 1
        return total
