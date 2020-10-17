# title: reverse-only-letters
# detail: https://leetcode.com/submissions/detail/404330684/
# datetime: Sun Oct  4 17:59:24 2020
# runtime: 24 ms
# memory: 13.9 MB

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        i, j = 0, len(S) - 1
        while i < j:
            if S[i].isalpha() and S[j].isalpha():
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
            elif S[i].isalpha():
                j -= 1
            elif S[j].isalpha():
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(S)