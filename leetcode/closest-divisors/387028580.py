# title: closest-divisors
# detail: https://leetcode.com/submissions/detail/387028580/
# datetime: Thu Aug 27 15:43:55 2020
# runtime: 216 ms
# memory: 13.7 MB

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        r = int(math.sqrt(num + 2))
        for a in range(r, -1, -1):
            b, c = divmod(num + 1, a)
            if c == 0:
                return a, b
            if c + 1 == a:
                return a, b + 1
        