# title: longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
# detail: https://leetcode.com/submissions/detail/382719099/
# datetime: Tue Aug 18 22:35:49 2020
# runtime: 700 ms
# memory: 23.9 MB

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = collections.deque()
        minq = collections.deque()
        result = 0
        l = 0
        for i, a in enumerate(nums):
            while maxq and a >= nums[maxq[-1]]:
                maxq.pop()
            while minq and a <= nums[minq[-1]]:
                minq.pop()
            maxq.append(i)
            minq.append(i)            
            if nums[maxq[0]] - nums[minq[0]] <= limit:
                l += 1
            else:
                if maxq[0] == i:
                    # a is the new max
                    j = i
                    while minq and a - nums[minq[0]] > limit:
                        j = minq.popleft()
                    l = i - j
                else:
                    # a is the new min
                    j = i
                    while maxq and nums[maxq[0]] - a > limit:
                        j = maxq.popleft()
                    l = i - j
            result = max(result, l)
        return result