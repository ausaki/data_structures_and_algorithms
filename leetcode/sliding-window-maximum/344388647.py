# title: sliding-window-maximum
# detail: https://leetcode.com/submissions/detail/344388647/
# datetime: Mon May 25 16:56:58 2020
# runtime: 344 ms
# memory: 26.3 MB

import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        res = [nums[q[0]]]
        for i in range(k, len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] < i - k + 1:
                q.popleft()
            res.append(nums[q[0]])
        return res