# title: number-of-matching-subsequences
# detail: https://leetcode.com/submissions/detail/411861771/
# datetime: Thu Oct 22 20:37:30 2020
# runtime: 468 ms
# memory: 15.2 MB

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        waiting = [[] for i in range(27)]
        for it in map(iter, words):
            waiting[ord(next(it)) - 97].append(it)
        for c in S:
            i = ord(c) - 97
            l, waiting[i] = waiting[i], []
            for it in l:
                waiting[ord(next(it, '{')) - 97].append(it)
        return len(waiting[-1])
    
                    