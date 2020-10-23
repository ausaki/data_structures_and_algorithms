# title: number-of-matching-subsequences
# detail: https://leetcode.com/submissions/detail/411858110/
# datetime: Thu Oct 22 20:19:44 2020
# runtime: 448 ms
# memory: 17.2 MB

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        pos = [[] for i in range(26)]
        for i, c in enumerate(S):
            pos[ord(c) - 97].append(i)
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
                    