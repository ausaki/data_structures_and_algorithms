# title: valid-palindrome
# detail: https://leetcode.com/submissions/detail/190879789/
# datetime: Wed Nov 21 16:44:25 2018
# runtime: 92 ms
# memory: N/A

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        
        while i <= j:
            while i <= j and not s[i].isalnum():
                i += 1
            while i <= j and not s[j].isalnum():
                j -= 1
            if i <= j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        