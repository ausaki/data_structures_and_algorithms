# title: longest-increasing-subsequence
# detail: https://leetcode.com/submissions/detail/275278390/
# datetime: Sat Nov  2 17:46:23 2019
# runtime: 56 ms
# memory: 13.9 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seq = [nums[0]]
        for num in nums[1:]:
            i = self.binary_search(seq, num, 0, len(seq) - 1)
            if i >= len(seq):
                seq.append(num)
            seq[i] = num
        return len(seq)
    
    
    def binary_search(self, nums, num, left, right):
        if left > right:
            return left
        middle = (left + right) // 2
        if nums[middle] == num:
            return middle
        if nums[middle] < num:
            return self.binary_search(nums, num, middle + 1, right)
        return self.binary_search(nums, num, left, middle - 1)
        
        