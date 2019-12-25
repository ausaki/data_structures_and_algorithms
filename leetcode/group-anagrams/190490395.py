# title: group-anagrams
# detail: https://leetcode.com/submissions/detail/190490395/
# datetime: Mon Nov 19 18:03:51 2018
# runtime: 160 ms
# memory: N/A

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            d.setdefault(tuple(counts), []).append(s)
        return d.values()
        