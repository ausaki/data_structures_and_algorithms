# title: longest-uncommon-subsequence-ii
# detail: https://leetcode.com/submissions/detail/283441445/
# datetime: Tue Dec  3 21:23:12 2019
# runtime: 32 ms
# memory: 12.7 MB

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def _issubseq(s1, s2):
            if len(s1) > len(s2):
                return False
            i = 0
            for ch in s2:
                if ch == s1[i]:
                    i += 1
                    if i == len(s1):
                        return True
            return False
        
        strs = sorted(strs, key=len, reverse=True)
        for i, s1 in enumerate(strs):
            if all(not _issubseq(s1, s2) for j, s2 in enumerate(strs) if j != i):
                return len(s1)
        return -1
        
            
        