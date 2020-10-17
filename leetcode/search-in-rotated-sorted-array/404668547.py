# title: search-in-rotated-sorted-array
# detail: https://leetcode.com/submissions/detail/404668547/
# datetime: Mon Oct  5 12:13:57 2020
# runtime: 40 ms
# memory: 14.3 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i, j = 0, n - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] > nums[-1]:
                i = m + 1
            else:
                j = m - 1
        # A[i] = min(nums), A[j] = max(nums)
        j = bisect.bisect_left(nums, target, 0, i)
        if j < i and nums[j] == target:
            return j
        j = bisect.bisect_left(nums, target, i, n)
        if j < n and nums[j] == target:
            return j
        return -1