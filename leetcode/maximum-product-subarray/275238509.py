# title: maximum-product-subarray
# detail: https://leetcode.com/submissions/detail/275238509/
# datetime: Sat Nov  2 13:02:13 2019
# runtime: 68 ms
# memory: 14.2 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        
        prev_max_product = nums[0]
        prev_min_product = nums[0]
        
        for num in nums[1:]:
            mi = num * prev_max_product
            mj = num * prev_min_product
            prev_max_product = max(num, mi, mj)
            prev_min_product = min(num, mi, mj)
            if prev_max_product > max_product:
                max_product = prev_max_product
        return max_product
        