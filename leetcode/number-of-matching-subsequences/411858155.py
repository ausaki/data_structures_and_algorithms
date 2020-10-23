# title: number-of-matching-subsequences
# detail: https://leetcode.com/submissions/detail/411858155/
# datetime: Thu Oct 22 20:19:58 2020
# runtime: 240 ms
# memory: 15.3 MB

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        result = 0
        for w, cnt in collections.Counter(words).items():
            i = 0
            for c in w:
                i = S.find(c, i)
                if i == -1:
                    break
                i += 1
            else:
                result += cnt
        return result
                    