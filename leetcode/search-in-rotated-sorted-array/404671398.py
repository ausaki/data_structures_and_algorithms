# title: search-in-rotated-sorted-array
# detail: https://leetcode.com/submissions/detail/404671398/
# datetime: Mon Oct  5 12:21:31 2020
# runtime: 40 ms
# memory: 14.4 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1
        