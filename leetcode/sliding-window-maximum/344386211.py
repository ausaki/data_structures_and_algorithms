# title: sliding-window-maximum
# detail: https://leetcode.com/submissions/detail/344386211/
# datetime: Mon May 25 16:47:48 2020
# runtime: 328 ms
# memory: 26.5 MB

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [0]
        for i in range(1, k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        res = [nums[q[0]]]
        for i in range(k, len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] < i - k + 1:
                q.pop(0)
            res.append(nums[q[0]])
        return res