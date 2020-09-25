# title: minimum-distance-to-type-a-word-using-two-fingers
# detail: https://leetcode.com/submissions/detail/391855577/
# datetime: Sun Sep  6 22:51:35 2020
# runtime: 360 ms
# memory: 35.2 MB

class Solution:
    def minimumDistance(self, word: str) -> int:
        l = len(word)
        m = 5
        n = 6
        @lru_cache(None)
        def tap(i, j, k):
            if i == l:
                return 0
            a = ord(word[i]) - ord('A')
            r, c = divmod(a, n)
            jr, jc = divmod(j, n) if j >= 0 else (r, c)
            kr, kc = divmod(k, n) if k >= 0 else (r, c)
            return min(abs(r - jr) + abs(c - jc) + tap(i + 1, a, k),
                       abs(r - kr) + abs(c - kc) + tap(i + 1, j, a))
        
        return tap(0, -1, -1)