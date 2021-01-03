# title: jump-game-vi
# detail: https://leetcode.com/submissions/detail/432467504/
# datetime: Sun Dec 20 11:22:46 2020
# runtime: 988 ms
# memory: 27.9 MB

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = collections.deque()
        dp.append((nums[n - 1], n - 1))
        for i in range(n - 2, -1, -1):
            while dp and dp[-1][1] > i + k:
                dp.pop()
            m = nums[i] + dp[-1][0]
            while dp and m >= dp[0][0]:
                dp.popleft()
            dp.appendleft((m, i))
        return dp[0][0]