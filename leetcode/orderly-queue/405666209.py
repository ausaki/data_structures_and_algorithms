# title: orderly-queue
# detail: https://leetcode.com/submissions/detail/405666209/
# datetime: Wed Oct  7 18:49:53 2020
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        n = len(S)
        if K >= 2:
            return ''.join(sorted(S))
        j = 0
        for i in range(1, n):
            if S[i] > S[j]:
                continue
            if S[i] < S[j]:
                j = i
                continue
            for k in range(i - j):
                if S[(i + k) % n] != S[j + k]:
                    if S[i + k] < S[j + k]:
                        j = i
                    break
        return S[j:] + S[:j]
            
                
                
                