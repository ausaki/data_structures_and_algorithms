# title: 4sum
# detail: https://leetcode.com/submissions/detail/282628861/
# datetime: Sat Nov 30 14:31:53 2019
# runtime: 1264 ms
# memory: 12.7 MB

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def _twosum(target, lo, hi):
            res = []
            while lo < hi:
                s = nums[lo] + nums[hi]
                if s == target:
                    # if not res or nums[lo] != res[-1][0] or nums[hi] != res[-1][1]:
                    #     res.append([nums[lo], nums[hi]])
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                elif s > target:
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                else:
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                
            return res
        
        nums.sort()
        i = 0
        N = len(nums)
        res = []
        while i + 3 < N:
            j = i + 1
            while j < N - 2:
                s = nums[i] + nums[j]
                two = _twosum(target - s, j + 1, N - 1)
                for t in two:
                    res.append([nums[i], nums[j], t[0], t[1]])
                j += 1
                while j < N - 2 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while i < N - 3 and nums[i] == nums[i - 1]:
                i += 1
        return res
        