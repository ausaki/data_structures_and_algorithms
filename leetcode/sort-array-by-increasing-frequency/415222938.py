# title: sort-array-by-increasing-frequency
# detail: https://leetcode.com/submissions/detail/415222938/
# datetime: Sat Oct 31 22:32:45 2020
# runtime: 60 ms
# memory: 14.3 MB

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        return sorted(nums, key=lambda k: (cnt[k], -k))