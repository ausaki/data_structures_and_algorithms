# title: max-consecutive-ones-iii
# detail: https://leetcode.com/submissions/detail/401378206/
# datetime: Sun Sep 27 20:42:08 2020
# runtime: 620 ms
# memory: 14.7 MB

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i, j, k, n = 0, 0, 0, len(A)
        result = 0
        while j < n:
            if A[j] == 0:
                K -= 1
                while K < 0:
                    if A[i] == 0:
                        K += 1
                    i += 1
            result = max(result, j - i + 1)
            j += 1
        return result