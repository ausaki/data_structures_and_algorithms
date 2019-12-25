# title: multiply-strings
# detail: https://leetcode.com/submissions/detail/140256802/
# datetime: Sat Feb 10 18:14:39 2018
# runtime: 743 ms
# memory: N/A

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        
        result_len = len1 + len2
        
        result = ''
        for i, c in enumerate(num2[::-1]):
            res = self._multiply(num1, c)
            if result == '':
                result = res
                continue
            if res == '0':
                continue
            result = self._add(result, res, i)
        return result
    
    def _multiply(self, num1, n):
        carry = 0
        n = int(n)
        result = ''
        
        if n == 0:
            return '0'
        
        for c in num1[::-1]:
            c = int(c)
            res = c * n + carry
            carry, remainder = divmod(res, 10)
            result = str(remainder) + result
        if carry > 0:
            result = str(carry) + result
        return result
        
    def _add(self, num1, num2, n):
        carry = 0
        result = num1[-n:]
        
        len1 = len(num1)
        len2 = len(num2)
        i = len1 - 1
        j = len2 - 1
        
        result = num1[-n :]
        i -= n
        if len1 - n < 0:
            result = ('0' * abs(len1 - n)) + result
        
        while i >= 0 and j >= 0:
            c1 = int(num1[i])
            c2 = int(num2[j])
            res = c1 + c2 + carry
            carry, remainder = divmod(res, 10)
            result = str(remainder) + result  
            i -= 1
            j -= 1
        
        while j >= 0:
            c2 = int(num2[j])
            res = c2 + carry
            carry, remainder = divmod(res, 10)
            result = str(remainder) + result  
            j -= 1
        
        if carry > 0:
            result = str(carry) + result
        return result
    