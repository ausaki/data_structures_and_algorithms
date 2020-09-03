# title: subarray-product-less-than-k
# detail: https://leetcode.com/submissions/detail/288668166/
# datetime: Thu Dec 26 17:26:01 2019
# runtime: 1244 ms
# memory: 16.9 MB

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left = 0
        right = 0
        product = 1
        res = 0
        while right < N:
            if product * nums[right] < k:
                product *= nums[right]
                right += 1
            else:
                if left == right:
                    left += 1
                    right += 1
                    product = 1
                else:
                    res += right - left
                    product //= nums[left]
                    left += 1    
        if product < k:
            return res + (right - left) * (1 + right - left) // 2
        else:
            return res
                
                        