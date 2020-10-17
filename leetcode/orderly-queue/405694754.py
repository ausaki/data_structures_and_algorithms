# title: orderly-queue
# detail: https://leetcode.com/submissions/detail/405694754/
# datetime: Wed Oct  7 20:58:28 2020
# runtime: 24 ms
# memory: 14.2 MB

class Solution(object):
    def orderlyQueue(self, S, K):
        if K == 1:
            return min(S[i:] + S[:i] for i in range(len(S)))
        return "".join(sorted(S))