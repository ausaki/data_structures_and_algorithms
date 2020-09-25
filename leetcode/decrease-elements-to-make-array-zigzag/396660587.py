# title: decrease-elements-to-make-array-zigzag
# detail: https://leetcode.com/submissions/detail/396660587/
# datetime: Thu Sep 17 01:45:45 2020
# runtime: 48 ms
# memory: 13.9 MB

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        for i in range(1, n, 2):
            if not (nums[i] < nums[i - 1] and (i + 1 >= n or nums[i] < nums[i + 1])):
                a += nums[i] - min(nums[i - 1], nums[i + 1] if i + 1 < n else 2000) + 1
        b = 0
        for i in range(0, n, 2):
            if not ((i - 1 < 0 or nums[i] < nums[i - 1]) and (i + 1 >= n or nums[i] < nums[i + 1])):
                b += nums[i] - min(nums[i - 1] if i - 1 >= 0 else 2000, nums[i + 1] if i + 1 < n else 2000) + 1
        return min(a, b)
        
        