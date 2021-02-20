# title: longest-nice-substring
# detail: https://leetcode.com/submissions/detail/458396692/
# datetime: Sat Feb 20 23:40:11 2021
# runtime: 84 ms
# memory: 14.4 MB

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        max_len = 0
        pos = -1
        for i in range(n):
            cnt = {}
            k = 0
            for j in range(i, n):
                a = s[j].lower()
                v = 1 if a == s[j] else 2
                if a not in cnt:
                    cnt[a] = v
                    k += 1
                elif (v & cnt[a]) == 0:
                    cnt[a] |= v
                    k -= 1
                if k == 0:
                    l = j - i + 1
                    if l > max_len:
                        max_len = l
                        pos = i
        return s[pos:pos + max_len]
                
                        