# title: find-the-smallest-divisor-given-a-threshold
# detail: https://leetcode.com/submissions/detail/393633857/
# datetime: Thu Sep 10 14:46:09 2020
# runtime: 372 ms
# memory: 19.1 MB

class Solution:
    def smallestDivisor(self, A, threshold):
        l, r = 1, max(A)
        while l < r:
            m = (l + r) // 2
            if sum((i + m - 1) // m for i in A) > threshold:
                l = m + 1
            else:
                r = m
        return l
            
        
        