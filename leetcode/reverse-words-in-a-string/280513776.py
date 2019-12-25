# title: reverse-words-in-a-string
# detail: https://leetcode.com/submissions/detail/280513776/
# datetime: Thu Nov 21 11:54:18 2019
# runtime: 52 ms
# memory: 13.7 MB

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(reversed(s))
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == ' ':
                j += 1
            if j == len(s):
                break
            spaces = j - i
            if spaces >= 1:
                if i == 0:
                    spaces += 1
                else:
                    i += 1
            while j < len(s) and s[j] != ' ':
                if spaces > 1:
                    s[j - spaces + 1] = s[j]
                    s[j] = ' '
                j += 1
            if spaces > 1:
                j -= spaces
            else:
                j -= 1
            k = i
            m = j
            while k < m:
                s[k], s[m] = s[m], s[k]
                k += 1
                m -= 1
            i = j + 1
        return ''.join(s[:i])
            
                
            
            
        