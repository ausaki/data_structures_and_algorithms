# title: increasing-triplet-subsequence
# detail: https://leetcode.com/submissions/detail/284973538/
# datetime: Tue Dec 10 15:02:41 2019
# runtime: 56 ms
# memory: 13.5 MB

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        i = 0
        a = b = -1
        while i < N - 1:
            if nums[i] < nums[i + 1]:
                if b == -1:
                    a = nums[i]
                    b = nums[i + 1]
                else:
                    if nums[i] > b or nums[i] > a or nums[i + 1] > b:
                        return True
                    a = nums[i]
                    b = nums[i + 1]
            i += 1
        return False