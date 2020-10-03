# title: n-repeated-element-in-size-2n-array
# detail: https://leetcode.com/submissions/detail/402617346/
# datetime: Wed Sep 30 16:35:30 2020
# runtime: 188 ms
# memory: 15.3 MB

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s = set()
        for a in A:
            if a in s:
                return a
            s.add(a)