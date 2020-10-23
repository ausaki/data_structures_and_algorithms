# title: number-of-matching-subsequences
# detail: https://leetcode.com/submissions/detail/411856359/
# datetime: Thu Oct 22 20:11:24 2020
# runtime: 672 ms
# memory: 17.3 MB

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        pos = [[] for i in range(26)]
        for i, c in enumerate(S):
            pos[ord(c) - 97].append(i)
        result = 0
        for w in words:
            i = -1
            for c in w:
                idx = pos[ord(c) - 97]
                j = bisect.bisect(idx, i)
                if j == len(idx):
                    break
                i = idx[j]
            else:
                result += 1
        return result
                    