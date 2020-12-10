# title: distribute-repeating-integers
# detail: https://leetcode.com/submissions/detail/420525203/
# datetime: Sun Nov 15 22:55:56 2020
# runtime: 2444 ms
# memory: 25.7 MB

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        if len(nums) < sum(quantity):
            return False
        buckets = sorted(collections.Counter(nums).values())
        quantity.sort()
        n = len(buckets)
        m = len(quantity)
        q = [0]
        for i in range(1, 1 << m):
            j = i.bit_length() - 1
            q.append(quantity[j] + q[i & ~(1 << j)])
        dp = [0] * (1 << m)
        dp[0] = True
        for i in range(n - 1, -1, -1):
            dp2 = []
            for mask in range(1 << m):
                if dp[mask]:
                    dp2.append(True)
                    continue
                k = False
                sub = mask
                while sub:
                    if buckets[i] >= q[sub] and dp[mask & ~sub]:
                        k = True
                        break
                    sub = (sub - 1) & mask
                dp2.append(k)
            dp = dp2
        return dp[-1]