# title: matchsticks-to-square
# detail: https://leetcode.com/submissions/detail/286370907/
# datetime: Mon Dec 16 20:06:12 2019
# runtime: 32 ms
# memory: 12.8 MB

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        def comb(i, target, result):
            if target == 0:
                return True
            if target < 0 or i < 0:
                return False
            result.append(i)
            if comb(i - 1, target - nums[i], result):
                return True
            result.pop()
            return comb(i - 1, target, result)
        S = sum(nums)
        if S % 4: return False
        N = len(nums)
        if N <= 3: return False
        q = S // 4
        nums.sort()
        for i in range(4):
            s = [N - 1]
            if not comb(N - 2, q - nums[N - 1], s):
                return False
            for i in s:
                nums.pop(i)
            N -= len(s)
        return True
        
        