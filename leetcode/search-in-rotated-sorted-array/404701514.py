# title: search-in-rotated-sorted-array
# detail: https://leetcode.com/submissions/detail/404701514/
# datetime: Mon Oct  5 13:46:34 2020
# runtime: 28 ms
# memory: 14.4 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i, j = 0, n - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            if nums[m] > nums[-1]:
                if nums[i] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            else:
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1
        return -1
        