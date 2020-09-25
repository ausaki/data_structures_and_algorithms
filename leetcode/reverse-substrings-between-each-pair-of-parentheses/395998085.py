# title: reverse-substrings-between-each-pair-of-parentheses
# detail: https://leetcode.com/submissions/detail/395998085/
# datetime: Tue Sep 15 15:42:55 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def reverseParentheses(self, s: str) -> str:
        return self.reverse(s)
    def reverse(self,s,i=0):
        res = ""
        while i < len(s):
            if s[i] == "(":
                new,i = self.reverse(s,i+1)
                res += new[::-1]
            elif s[i] == ")":
                return res,i
            else:
                res += s[i]
            i += 1
        return res
            