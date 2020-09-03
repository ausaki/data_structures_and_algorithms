# title: four-divisors
# detail: https://leetcode.com/submissions/detail/375483580/
# datetime: Tue Aug  4 00:40:35 2020
# runtime: 352 ms
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
                if num % d == 0:
                    if a == 0 and b == 0:
                        a = d
                        b = num // d
                    else:
                        break
            else:
                if a > 0:
                    result += a + b + 1 + num
        return result