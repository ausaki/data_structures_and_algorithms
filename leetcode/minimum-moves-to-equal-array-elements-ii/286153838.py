# title: minimum-moves-to-equal-array-elements-ii
# detail: https://leetcode.com/submissions/detail/286153838/
# datetime: Mon Dec 16 00:24:40 2019
# runtime: 88 ms
# memory: 14.1 MB

import heapq
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1: return 0
        middle = heapq.nsmallest(N // 2 + 1, nums)[-1]
        print(middle)
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