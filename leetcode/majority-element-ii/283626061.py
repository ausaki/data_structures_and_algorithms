# title: majority-element-ii
# detail: https://leetcode.com/submissions/detail/283626061/
# datetime: Wed Dec  4 14:48:10 2019
# runtime: 128 ms
# memory: 14 MB

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        onethird = N // 3
        a = 0
        a_cnt = 0
        b = 0
        b_cnt = 0
        for i in nums:
            if a == i:
                a_cnt += 1
            elif b == i:
                b_cnt += 1
            elif a_cnt == 0:
                a = i
                a_cnt = 1
            elif b_cnt == 0:
                b = i
                b_cnt = 1
            else:
                a_cnt -= 1
                b_cnt -= 1
        res = []
        a_cnt = 0
        b_cnt = 0
        for i in nums:
            if a == i:
                a_cnt += 1
            elif b == i:
                b_cnt += 1
        if a_cnt > onethird:
            res.append(a)
        if b_cnt > onethird:
            res.append(b)
        return res
