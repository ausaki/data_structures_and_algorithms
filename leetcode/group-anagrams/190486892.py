# title: group-anagrams
# detail: https://leetcode.com/submissions/detail/190486892/
# datetime: Mon Nov 19 17:26:13 2018
# runtime: 124 ms
# memory: N/A

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            d.setdefault(''.join(sorted(s)), []).append(s)
        return d.values()
        