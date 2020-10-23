# title: number-of-matching-subsequences
# detail: https://leetcode.com/submissions/detail/411857510/
# datetime: Thu Oct 22 20:17:03 2020
# runtime: 656 ms
# memory: 17.1 MB

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        pos = [[] for i in range(26)]
        for i, c in enumerate(S):
            pos[ord(c) - 97].append(i)
        result = 0
        for w, cnt in collections.Counter(words).items():
            i = -1
            for c in w:
                idx = pos[ord(c) - 97]
                j = bisect.bisect(idx, i)
                if j == len(idx):
                    break
                i = idx[j]
            else:
                result += cnt
        return result
                    