# title: the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
# detail: https://leetcode.com/submissions/detail/383635252/
# datetime: Thu Aug 20 16:34:49 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # 3 * (2 ^ (n - 1))
        all_strs = []
        mp = {'a': 'bc', 'b': 'ac', 'c': 'ab'}
        def gen(prev, k):
            l = len(prev)
            if l == n:
                return prev
            m = 1 << (n - l - 1)
            if k <= m:
                return gen(prev + mp[prev[-1]][0], k)
            return gen(prev + mp[prev[-1]][1], k - m)
        
        N = 3 * (1 << (n - 1))
        if k > N:
            return ''
        m = 1 << (n - 1)
        if k <= m:
            return gen('a', k)
        elif k <= 2 * m:
            return gen('b', k - m)
        else:
            return gen('c', k - 2 * m)
