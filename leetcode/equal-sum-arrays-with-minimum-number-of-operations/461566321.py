# title: equal-sum-arrays-with-minimum-number-of-operations
# detail: https://leetcode.com/submissions/detail/461566321/
# datetime: Sun Feb 28 12:51:02 2021
# runtime: 1288 ms
# memory: 20.4 MB

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
		# determine which is larger and get the difference on sum
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        if sum1==sum2:
            return 0
        elif sum1>sum2:
            larger_sum_nums = nums1
            smaller_sum_nums = nums2
        else:
            larger_sum_nums = nums2
            smaller_sum_nums = nums1
            
        sum_diff = abs(sum1-sum2)
            
        # calculate the max "gain" at each position (how much difference we can reduce if operating on the position)    
        larger_sum_nums_diff = [num-1 for num in larger_sum_nums]
        smaller_sum_nums_diff = [6-num for num in smaller_sum_nums]
        
        sum_nums_diff = larger_sum_nums_diff+smaller_sum_nums_diff
        
		# sort the "gain" and check the least number of steps to reduce that difference to 0
        sum_nums_diff.sort(reverse = True)
        
        count = 0
        target_diff = sum_diff
        
        for i in range(len(sum_nums_diff)):
            target_diff -= sum_nums_diff[i]
            count += 1
            
            if target_diff <= 0:
                return count
        return -1
