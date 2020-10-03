# title: equal-rational-numbers
# detail: https://leetcode.com/submissions/detail/402594242/
# datetime: Wed Sep 30 15:17:15 2020
# runtime: 32 ms
# memory: 14 MB

from fractions import Fraction

class Solution(object):
    def isRationalEqual(self, S, T):
        def convert(S):
            if '.' not in S:
                return Fraction(int(S), 1)
            i = S.index('.')
            ans = Fraction(int(S[:i]), 1)
            S = S[i+1:]
            if '(' not in S:
                if S:
                    ans += Fraction(int(S), 10 ** len(S))
                return ans

            i = S.index('(')
            if i:
                ans += Fraction(int(S[:i]), 10 ** i)
            S = S[i+1:-1]
            j = len(S)
            ans += Fraction(int(S), 10**i * (10**j - 1))
            return ans
        
        s = convert(S)
        t = convert(T)
        return s == t