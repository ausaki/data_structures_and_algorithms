# title: maximum-number-of-vowels-in-a-substring-of-given-length
# detail: https://leetcode.com/submissions/detail/381729920/
# datetime: Sun Aug 16 21:51:12 2020
# runtime: 140 ms
# memory: 14.6 MB

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0
        m = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in m:
                cnt += 1
        result = cnt
        for i in range(i + 1, len(s)):
            if s[i] in m:
                cnt += 1
            if s[i - k]  in m:
                cnt -= 1
            result = max(result, cnt)
        return result