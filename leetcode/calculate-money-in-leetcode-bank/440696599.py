# title: calculate-money-in-leetcode-bank
# detail: https://leetcode.com/submissions/detail/440696599/
# datetime: Sat Jan  9 22:41:49 2021
# runtime: 60 ms
# memory: 14.1 MB

class Solution:
    def totalMoney(self, n: int) -> int:
        q, r = divmod(n, 7)
        return sum(28 + i * 7 for i in range(q)) + sum(1 + i + q for i in range(r))