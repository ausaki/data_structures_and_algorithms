# title: count-substrings-that-differ-by-one-character
# detail: https://leetcode.com/submissions/detail/415232828/
# datetime: Sat Oct 31 22:55:55 2020
# runtime: 2544 ms
# memory: 123.1 MB

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        S, T = len(s), len(t)
        cnt = collections.defaultdict(collections.Counter)
        for i in range(T):
            for j in range(i + 1):
                x = t[j:i + 1]
                for k in range(len(x)):
                    cnt[x[:k] + '*' + x[k + 1:]][x[k]] += 1
        result = 0
        for i in range(S):
            for j in range(i + 1):
                x = s[j:i + 1]
                for k in range(len(x)):
                    c = cnt[x[:k] + '*' + x[k + 1:]]
                    result += sum(c.values()) - c[x[k]]
        return result