# title: decompress-run-length-encoded-list
# detail: https://leetcode.com/submissions/detail/391857582/
# datetime: Sun Sep  6 22:58:11 2020
# runtime: 72 ms
# memory: 14.1 MB

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [nums[i + 1] for i in range(0, len(nums), 2) for j in range(nums[i])]
