# title: minimum-number-of-k-consecutive-bit-flips
# detail: https://leetcode.com/submissions/detail/401723577/
# datetime: Mon Sep 28 15:16:30 2020
# runtime: 796 ms
# memory: 20.3 MB

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        def flip(i):
            if i == n:
                return 0
            if A[i] == 1:
                return flip(i + 1)
            if n - i < K:
                return M
            for j in range(K):
                A[i + j] = (A[i + j] + 1) % 2
            return flip(i + 1) + 1
        n = len(A)
        result = 0
        flips = collections.deque()
        for i, j in enumerate(A):
            while flips and flips[0] < i:
                flips.popleft()
            j = (j + len(flips) % 2) % 2
            if j == 0:
                result += 1
                if i + K - 1 >= n:
                    return -1
                flips.append(i + K - 1)
        return result