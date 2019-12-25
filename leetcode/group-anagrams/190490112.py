# title: group-anagrams
# detail: https://leetcode.com/submissions/detail/190490112/
# datetime: Mon Nov 19 18:00:49 2018
# runtime: 136 ms
# memory: N/A

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            d.setdefault(tuple(sorted(s)), []).append(s)
        return d.values()
        