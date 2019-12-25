# title: add-binary
# detail: https://leetcode.com/submissions/detail/145540762/
# datetime: Sat Mar 17 17:00:38 2018
# runtime: 64 ms
# memory: N/A

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ''
        len_a = len(a)
        len_b = len(b)
        n = min(len_a, len_b)
        i = len_a - 1
        j = len_b - 1
        
        while i >= 0 and j >= 0:
            s = int(a[i]) + int(b[j]) + carry
            carry, r = divmod(s, 2)
            result = str(r) + result
            i -= 1
            j -= 1
        
        print i, j, result
            
        while i >= 0:
            s = int(a[i]) + carry
            carry, r = divmod(s, 2)
            result = str(r) + result
            i -= 1
            
        while j >= 0:
            s = int(b[j]) + carry
            carry, r = divmod(s, 2)
            result = str(r) + result
            j -= 1
        
        if carry > 0:
            result = str(carry) + result
        
        return result
        
                
        