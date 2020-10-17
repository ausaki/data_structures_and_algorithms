# title: find-and-replace-pattern
# detail: https://leetcode.com/submissions/detail/405973156/
# datetime: Thu Oct  8 11:41:00 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            p = {}
            s = set()
            for a, b in zip(pattern, word):
                if a not in p:
                    if b in s:
                        break
                    p[a] = b
                    s.add(b)
                elif p[a] != b:
                    break
            else:
                result.append(word)
        return result