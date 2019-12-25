# title: minimum-moves-to-equal-array-elements-ii
# detail: https://leetcode.com/submissions/detail/286152729/
# datetime: Mon Dec 16 00:16:43 2019
# runtime: 76 ms
# memory: 13.9 MB

import heapq
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if not nums: return 0
        N = len(nums)
        nums.sort()
        middle = nums[N // 2]
        res = 0
        for num in nums:
            res += abs(num - middle)
        return res
        # y = nums[0]
        # s1 = sum(num - y for num in nums)
        # s2 = 0
        # res = s1 + s2
        # for i in range(1, N):
        #     dy = nums[i] - y
        #     s1 = s1 - (N - i) * dy
        #     s2 += dy * i
        #     y = nums[i]
        #     print(i, s1, s2, s1 + s2)
        #     res = min(res, s1 + s2)
            
        return res