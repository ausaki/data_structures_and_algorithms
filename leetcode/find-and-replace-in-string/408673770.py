# title: find-and-replace-in-string
# detail: https://leetcode.com/submissions/detail/408673770/
# datetime: Wed Oct 14 23:31:01 2020
# runtime: 36 ms
# memory: 14.3 MB

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        repl = {}
        for i, s, t in zip(indexes, sources, targets):
            repl[i] = [s, t]
        i = 0
        result = ''
        n = len(S)
        while i < n:
            s, t = repl.get(i, [S[i], S[i]])
            if S.startswith(s, i):
                result += t
                i += len(s)
            else:
                result += S[i]
                i += 1
        return result
                