# title: preimage-size-of-factorial-zeroes-function
# detail: https://leetcode.com/submissions/detail/411914526/
# datetime: Thu Oct 22 23:50:37 2020
# runtime: 24 ms
# memory: 14.1 MB

class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        '''
        the number of trailing zeros of x! equals to the number of factors 5
        '''
        def count(x):
            cnt = 0
            while x >= 5:
                x //= 5
                cnt += x 
            return cnt
        if K == 0:
            return 5
        l, r = 5, 5 * K
        while l <= r:
            m = (l + r) // 2
            cnt = count(m)
            if cnt < K:
                l = m + 1
            else:
                r = m - 1
        return 5 if count(l) == K else 0
            