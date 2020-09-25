# title: greatest-sum-divisible-by-three
# detail: https://leetcode.com/submissions/detail/394164845/
# datetime: Fri Sep 11 19:15:43 2020
# runtime: 244 ms
# memory: 18.7 MB

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        o1, o2 = 1e5, 1e5
        t1, t2 = 1e5, 1e5
        s = 0
        for num in nums:
            r = num % 3
            if r == 1:
                if num < o1:
                    o1, o2 = num, o1
                elif num < o2:
                    o2 = num
            elif r == 2:
                if num < t1:
                    t1, t2 = num, t1
                elif num < t2:
                    t2 = num
            s += num
        r = s % 3
        if r == 0:
            return s
        if r == 1:
            s -= min(o1, t1 + t2)
        else:
            s -= min(t1, o1 + o2)
        return s
            