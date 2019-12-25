# title: 132-pattern
# detail: https://leetcode.com/submissions/detail/281564929/
# datetime: Mon Nov 25 20:43:22 2019
# runtime: 140 ms
# memory: 14.5 MB

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = [nums[-1]]
        ak = None
        for num in nums[-2::-1]:
            if ak is not None and num < ak:
                return True
            while stack and num > stack[-1]:
                ak = stack.pop()
            stack.append(num)
        return False
        