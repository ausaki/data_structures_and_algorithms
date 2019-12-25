# title: largest-divisible-subset
# detail: https://leetcode.com/submissions/detail/285006572/
# datetime: Tue Dec 10 18:47:33 2019
# runtime: 384 ms
# memory: 12.9 MB

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        dp = {1: set()}
        nums.sort()
        for num in nums:
            dp[num] = set([num]) | max([s for n, s in dp.items() if num % n == 0], key=len)
        return list(max(dp.values(), key=len))