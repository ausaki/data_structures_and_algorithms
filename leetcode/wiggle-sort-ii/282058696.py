# title: wiggle-sort-ii
# detail: https://leetcode.com/submissions/detail/282058696/
# datetime: Wed Nov 27 21:51:27 2019
# runtime: 172 ms
# memory: 15.4 MB

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        nums.sort()
        mid = N // 2
        if N % 2 : nums[mid], nums[-1] = nums[-1], nums[mid]
        new_nums = []
        for i in reversed(range(mid)):
            new_nums.append(nums[i])
            new_nums.append(nums[mid + i])
        nums[:N - N % 2] = new_nums
                
         
