# title: increasing-triplet-subsequence
# detail: https://leetcode.com/submissions/detail/284973914/
# datetime: Tue Dec 10 15:04:27 2019
# runtime: 56 ms
# memory: 13.3 MB

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        i = 0
        a = b = -1
        while i < N - 1:
            if nums[i] < nums[i + 1]:
                if b == -1:
                    a = i
                    b = i + 1
                else:
                    if nums[i] > nums[b] or nums[i] > nums[a] or nums[i + 1] > nums[b]:
                        return True
                    a = i
                    b = i + 1
            i += 1
        return False