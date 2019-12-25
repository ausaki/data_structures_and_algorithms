# title: group-anagrams
# detail: https://leetcode.com/submissions/detail/190490069/
# datetime: Mon Nov 19 18:00:19 2018
# runtime: 128 ms
# memory: N/A

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            d.setdefault(tuple(sorted(s)), []).append(s)
        return list(d.values())
        
        