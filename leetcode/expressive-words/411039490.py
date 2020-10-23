# title: expressive-words
# detail: https://leetcode.com/submissions/detail/411039490/
# datetime: Tue Oct 20 20:17:17 2020
# runtime: 48 ms
# memory: 14.2 MB

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def group(s):
            if not s:
                return []
            g = [[s[0], 0]]
            for c in s:
                if c == g[-1][0]:
                    g[-1][1] += 1
                else:
                    g.append([c, 1])
            return g
        g = group(S)
        result = 0
        for word in words:
            wg = group(word)
            if len(g) != len(wg):
                continue
            for a, b in zip(g, wg):
                if a[0] != b[0] or b[1] > a[1] or (a[1] < 3 and a[1] > b[1]):
                    break
            else:
                result += 1
        return result