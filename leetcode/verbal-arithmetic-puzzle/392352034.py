# title: verbal-arithmetic-puzzle
# detail: https://leetcode.com/submissions/detail/392352034/
# datetime: Tue Sep  8 00:11:31 2020
# runtime: 496 ms
# memory: 14 MB

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        n = len(words)
        mapper = {}
        maxlen = 0
        for w in words:
            maxlen = max(maxlen, len(w))
            for c in w:
                mapper[c] = -1
        if len(result) < maxlen or len(result) - maxlen > 1:
            return False
        for c in result:
            mapper[c] = -1
        used = [0] * 10
        def solve(i, j, s):
            if j == n:
                l = len(result) - i
                if l < 0:
                    if s != 0:
                        return False
                    if any(mapper[w[0]] == 0 for w in words):
                        return False
                    if mapper[result[0]] == 0:
                        return False
                    return True
                c, s = divmod(s, 10)
                if mapper[result[l]] >= 0:
                    if mapper[result[l]] == s:
                        return solve(i + 1, 0, c)
                    return False
                if used[s]:
                    return False
                mapper[result[l]] = s
                used[s] = 1
                res = solve(i + 1, 0, c)
                mapper[result[l]] = -1
                used[s] = 0
                return res
            w = words[j]
            l = len(w) - i
            if l < 0:
                return solve(i, j + 1, s)
            if mapper[w[l]] >= 0:
                return solve(i, j + 1, s + mapper[w[l]])
            for k in range(10):
                if used[k]:
                    continue
                used[k] = 1
                mapper[w[l]] = k
                if solve(i, j + 1, s + k):
                    return True
                used[k] = 0
                mapper[w[l]] = -1
            return False
        return solve(1, 0, 0)