# title: restore-ip-addresses
# detail: https://leetcode.com/submissions/detail/147033485/
# datetime: Mon Mar 26 18:18:07 2018
# runtime: 39 ms
# memory: N/A

class Solution(object):
    def restoreIpAddresses_(self, s, n):
        result = []
        if not n <= len(s) <= 3 * n:
            return []
        
        if n == 1:
            
            if 0 <= int(s) <= 255 and (len(s) == 1 or s[0] != '0'):
                return [s]
            else:
                return []
        
        if 0<= int(s[:1]) <= 255:
            ip_list = self.restoreIpAddresses_(s[1:], n - 1)
            for item in ip_list:
                result.append(s[:1] + '.' + item)
        if 0<= int(s[:2]) <= 255 and s[0] != '0':
            ip_list = self.restoreIpAddresses_(s[2:], n - 1)
            for item in ip_list:
                result.append(s[:2] + '.' + item)
        if 0<= int(s[:3]) <= 255 and s[0] != '0':
            ip_list = self.restoreIpAddresses_(s[3:], n - 1)
            for item in ip_list:
                result.append(s[:3] + '.' + item)
        return result
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.restoreIpAddresses_(s, 4)
        
        