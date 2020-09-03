# title: number-of-ways-to-reorder-array-to-get-same-bst
# detail: https://leetcode.com/submissions/detail/390008694/
# datetime: Thu Sep  3 00:06:24 2020
# runtime: 260 ms
# memory: 18.9 MB

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        def C(n, m):
            s = 1
            for i in range(n, n - m, -1):
                s *= i
            for i in range(2, m + 1):
                s //= i
            # s = math.factorial(n) // math.factorial(n - m) // math.factorial(m)
            return s  % MOD
        
        def count(nums):
            n = len(nums)
            if n == 0:
                return 1
            left = []
            right = []
            for i in range(1, n):
                if nums[i] > nums[0]:
                    right.append(nums[i])
                else:
                    left.append(nums[i])
            l = count(left) 
            r = count(right)
            ll = len(left)
            return (l * r * C(n - 1, ll))  % MOD
        
        return (count(nums) - 1) % MOD