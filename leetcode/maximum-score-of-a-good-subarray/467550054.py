# title: maximum-score-of-a-good-subarray
# detail: https://leetcode.com/submissions/detail/467550054/
# datetime: Sun Mar 14 14:07:19 2021
# runtime: 1324 ms
# memory: 25.3 MB

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = k
        res = mi = nums[k]
        while i > 0 or j < n - 1:
            if (nums[i - 1] if i else 0) < (nums[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            mi = min(mi, nums[i], nums[j])
            res = max(res, mi * (j - i + 1))
        return res
        