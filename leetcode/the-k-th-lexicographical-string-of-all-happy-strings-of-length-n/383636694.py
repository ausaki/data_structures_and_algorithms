# title: the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
# detail: https://leetcode.com/submissions/detail/383636694/
# datetime: Thu Aug 20 16:39:58 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        mp = {'a': 'bc', 'b': 'ac', 'c': 'ab'}
        N = 3 * (1 << (n - 1))
        if k > N:
            return ''
        m = 1 << (n - 1)
        s = []
        if k <= m:
            s.append('a')
        elif k <= 2 * m:
            s.append('b')
            k -= m
        else:
            s.append('c')
            k -= 2 * m
        while True:
            l = len(s)
            if l == n:
                break
            m = 1 << (n - l - 1)
            if k <= m:
                s.append(mp[s[-1]][0])
            else:
                s.append(mp[s[-1]][1])
                k -= m
        return ''.join(s)
