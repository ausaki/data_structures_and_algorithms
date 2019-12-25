# title: total-hamming-distance
# detail: https://leetcode.com/submissions/detail/280091027/
# datetime: Tue Nov 19 19:04:51 2019
# runtime: 556 ms
# memory: 14 MB

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bucket = [0] * 32
        for num in nums:
            for i in range(32):
                if (1 << i) & num:
                    bucket[i] += 1
        total = 0
        for i in range(32):
            if bucket[i] > 0:
                total += bucket[i] * (len(nums) - bucket[i])
        return total
        