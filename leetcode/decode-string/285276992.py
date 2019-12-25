# title: decode-string
# detail: https://leetcode.com/submissions/detail/285276992/
# datetime: Thu Dec 12 00:17:57 2019
# runtime: 28 ms
# memory: 12.8 MB

class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        
        def decode(i):
            enc_str = ''
            j = i
            while j < N and s[j].isdigit():
                j += 1
            cnt = int(s[i: j])
            i = j + 1
            while i < N and s[i] != ']':
                j = i
                while j < N and s[j].isalpha():
                    j += 1
                enc_str += s[i: j]
                i = j
                if s[i].isdigit():
                    ss, i = decode(j)
                    enc_str += ss
            return enc_str * cnt, i + 1
        res = ''
        i = 0
        while i < N:
            if s[i].isdigit():
                ss, i = decode(i)
                res += ss
            else:
                j = i
                while j < N and s[j].isalpha():
                    j += 1
                res += s[i: j]
                i = j
        return res