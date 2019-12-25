# title: longest-word-in-dictionary-through-deleting
# detail: https://leetcode.com/submissions/detail/286615461/
# datetime: Tue Dec 17 19:17:43 2019
# runtime: 128 ms
# memory: 14.8 MB

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        return min(list(filter(isSubsequence, d)) + [''], key=lambda x: (-len(x), x))