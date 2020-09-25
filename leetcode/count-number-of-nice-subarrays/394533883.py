# title: count-number-of-nice-subarrays
# detail: https://leetcode.com/submissions/detail/394533883/
# datetime: Sat Sep 12 16:33:45 2020
# runtime: 892 ms
# memory: 20.8 MB

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        o1, o2 = -1, -1
        result = 0
        for i, j in enumerate(nums):
            if j % 2:
                if k > 1:
                    k -= 1
                    continue
                o1 = o2
                for o2 in range(o2 + 1, i + 1):
                    if nums[o2] % 2:
                        break
            result += o2 - o1
        return result
                