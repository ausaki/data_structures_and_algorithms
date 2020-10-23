# title: number-of-subarrays-with-bounded-maximum
# detail: https://leetcode.com/submissions/detail/411876887/
# datetime: Thu Oct 22 21:41:55 2020
# runtime: 316 ms
# memory: 15.4 MB

class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        mark = -1
        cnt = 0
        result = 0
        for i, a in enumerate(A):
            if L <= a <= R:
                cnt = i - mark 
                result += cnt 
            elif a < L:
                result += cnt
            else:
                mark = i
                cnt = 0
        return result