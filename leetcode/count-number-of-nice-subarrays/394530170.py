# title: count-number-of-nice-subarrays
# detail: https://leetcode.com/submissions/detail/394530170/
# datetime: Sat Sep 12 16:19:21 2020
# runtime: 860 ms
# memory: 20.3 MB

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = collections.deque([-1] * (k + 1))
        result = 0
        for i, j in enumerate(nums):
            if j % 2:
                l = odds.popleft()
                odds.append(i)
            result += odds[1] - odds[0]
        return result
                