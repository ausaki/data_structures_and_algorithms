# title: longest-word-in-dictionary-through-deleting
# detail: https://leetcode.com/submissions/detail/286615028/
# datetime: Tue Dec 17 19:13:22 2019
# runtime: 96 ms
# memory: 14.5 MB

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        mapping = collections.defaultdict(list)
        for i, c in enumerate(s):
            mapping[c].append(i)
        d.sort(key=len, reverse=True)
        res = ''
        for word in d:
            l = len(word)
            if l > len(s): 
                continue
            if l < len(res):
                break
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