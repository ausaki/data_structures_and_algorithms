# title: shuffle-the-array
# detail: https://leetcode.com/submissions/detail/371471491/
# datetime: Sun Jul 26 00:52:37 2020
# runtime: 56 ms
# memory: 14.2 MB

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        def gen(n):
            for i in range(n):
                yield nums[i]
                yield nums[n + i]
        return gen(n)
        
    
        # a = [0] * (2 * n)
        # for i in range(n):
        #     a[2 * i] = nums[i]
        #     a[2 * i + 1] = nums[n + i]
        # return a