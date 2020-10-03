# title: max-consecutive-ones-iii
# detail: https://leetcode.com/submissions/detail/401378269/
# datetime: Sun Sep 27 20:42:25 2020
# runtime: 640 ms
# memory: 14.6 MB

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i, j, n = 0, 0, len(A)
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