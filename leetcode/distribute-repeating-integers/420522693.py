# title: distribute-repeating-integers
# detail: https://leetcode.com/submissions/detail/420522693/
# datetime: Sun Nov 15 22:44:17 2020
# runtime: 2448 ms
# memory: 32.7 MB

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        @lru_cache(None)
        def dp(i, mask):
            if mask == 0:
                return True
            if i == n:
                return False
            sub = mask
            while sub:
                if buckets[i] >= q[sub] and dp(i + 1, mask & ~sub):
                    return True
                sub = (sub - 1) & mask
            return dp(i + 1, mask)
        
        if len(nums) < sum(quantity):
            return False
        buckets = sorted(collections.Counter(nums).values())
        n = len(buckets)
        m = len(quantity)
        q = [0]
        for i in range(1, 1 << m):
            j = i.bit_length() - 1
            q.append(quantity[j] + q[i & ~(1 << j)])
        return dp(0, (1 << m) - 1)