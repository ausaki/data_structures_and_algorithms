# title: subtract-the-product-and-sum-of-digits-of-an-integer
# detail: https://leetcode.com/submissions/detail/393556935/
# datetime: Thu Sep 10 11:29:16 2020
# runtime: 28 ms
# memory: 13.8 MB

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        while n:
            n, r = divmod(n, 10)
            p *= r
            s += r
        return p - s