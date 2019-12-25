# title: 132-pattern
# detail: https://leetcode.com/submissions/detail/281565572/
# datetime: Mon Nov 25 20:49:35 2019
# runtime: 140 ms
# memory: 14.3 MB

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3:
            return False
        sp = N - 1
        ak = None
        for num in nums[-2::-1]:
            if ak is not None and num < ak:
                return True
            while sp < N and num > nums[sp]:
                ak = nums[sp]
                sp += 1
            sp -= 1
            nums[sp] = num
        return False
        