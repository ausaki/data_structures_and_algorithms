# title: longest-word-in-dictionary-through-deleting
# detail: https://leetcode.com/submissions/detail/286611083/
# datetime: Tue Dec 17 18:31:18 2019
# runtime: 104 ms
# memory: 14.7 MB

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        mapping = collections.defaultdict(list)
        for i, c in enumerate(s):
            mapping[c].append(i)
        res = ''
        for word in d:
            l = len(word)
            if l > len(s) or l < len(res): 
                continue
            i = -1
            for c in word:
                if c not in mapping:
                    break
                j = bisect.bisect(mapping[c], i)
                if j >= len(mapping[c]):
                    break
                i = mapping[c][j]
            else:
                if l > len(res) or word < res:
                    res = word
        return res