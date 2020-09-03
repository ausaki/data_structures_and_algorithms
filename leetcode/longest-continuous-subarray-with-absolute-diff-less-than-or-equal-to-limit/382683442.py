# title: longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
# detail: https://leetcode.com/submissions/detail/382683442/
# datetime: Tue Aug 18 20:41:51 2020
# runtime: 4340 ms
# memory: 24 MB

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ma, mi =  0, 0
        l = 0
        result = 0
        n = len(nums)
        for i in range(n):
            # print(mi, ma, l)
            num = nums[i]
            if nums[mi] <= num <= nums[ma]:
                if num == nums[mi]:
                    mi = i
                if num == nums[ma]:
                    ma = i
                l += 1
                result = max(result, l)
                continue
            if num > nums[ma]:
                if num - nums[mi] <= limit:
                    l += 1
                    ma = i
                elif num - nums[ma] > limit:
                    mi = ma = i
                    l = 1
                else:
                    k = mi
                    mi = i
                    ma = i
                    l = 1
                    for j in range(i - 1, k, -1):
                        if num - nums[j] <= limit:
                            if nums[j] < nums[mi]:
                                mi = j
                            l += 1
                        else:
                            break
                result = max(result, l)
            else:
                if nums[ma] - num <= limit:
                    l += 1
                    mi = i
                elif nums[mi] - num > limit:
                    mi = ma = i
                    l = 1
                else:
                    k = ma
                    mi = i
                    ma = i
                    l = 1
                    for j in range(i - 1, k, -1):
                        if nums[j] - num <= limit:
                            if nums[j] > nums[ma]:
                                ma = j
                            l += 1
                        else:
                            break
                result = max(result, l)
        return result
            
            