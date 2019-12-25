# title: group-anagrams
# detail: https://leetcode.com/submissions/detail/190489663/
# datetime: Mon Nov 19 17:55:15 2018
# runtime: 148 ms
# memory: N/A

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            d.setdefault(''.join(sorted(s)), []).append(s)
        return list(d.values())
        
        