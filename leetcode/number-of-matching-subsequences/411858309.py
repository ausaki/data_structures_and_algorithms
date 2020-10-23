# title: number-of-matching-subsequences
# detail: https://leetcode.com/submissions/detail/411858309/
# datetime: Thu Oct 22 20:20:44 2020
# runtime: 284 ms
# memory: 15.4 MB

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        result = 0
        for w in words:
            i = 0
            for c in w:
                i = S.find(c, i)
                if i == -1:
                    break
                i += 1
            else:
                result += 1
        return result
                    