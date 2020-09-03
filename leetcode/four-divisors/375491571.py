# title: four-divisors
# detail: https://leetcode.com/submissions/detail/375491571/
# datetime: Tue Aug  4 01:00:52 2020
# runtime: 692 ms
# memory: 14.9 MB

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            root = int(math.sqrt(num))
            if root ** 2 == num:
                continue
            a, b = 0, 0
            for d in range(2, root + 1):
                q, r = divmod(num, d)
                if r == 0:
                    if b != 0:
                        break
                    a, b = q, d
            else:
                if b > 0:
                    result += a + b + 1 + num
        return result