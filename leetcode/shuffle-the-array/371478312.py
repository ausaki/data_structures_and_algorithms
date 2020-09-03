# title: shuffle-the-array
# detail: https://leetcode.com/submissions/detail/371478312/
# datetime: Sun Jul 26 01:11:23 2020
# runtime: 76 ms
# memory: 14 MB

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return reduce(add, zip(nums[:n], nums[n:]))
        
    
        # a = [0] * (2 * n)
        # for i in range(n):
        #     a[2 * i] = nums[i]
        #     a[2 * i + 1] = nums[n + i]
        # return a