# title: predict-the-winner
# detail: https://leetcode.com/submissions/detail/286326946/
# datetime: Mon Dec 16 14:44:26 2019
# runtime: 48 ms
# memory: 13.1 MB

from functools import lru_cache
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        @lru_cache(None)
        def play(i, j):
            if i > j:
                return 0
            player = (N - (j - i + 1)) % 2
            if player == 0:
                return max(nums[i] + play(i + 1, j), nums[j] + play(i, j - 1))
            else:
                return min(play(i + 1, j), play(i, j - 1))
        scores = play(0, N - 1)
        print(scores)
        return scores >= sum(nums) / 2
