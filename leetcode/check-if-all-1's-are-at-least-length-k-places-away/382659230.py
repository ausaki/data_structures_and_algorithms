# title: check-if-all-1's-are-at-least-length-k-places-away
# detail: https://leetcode.com/submissions/detail/382659230/
# datetime: Tue Aug 18 19:05:28 2020
# runtime: 612 ms
# memory: 17.2 MB

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        j = -k - 1
        for i, num in enumerate(nums):
            if num == 0:
                continue
            if i - j <= k:
                return False
            j = i
        return True
            