# title: max-consecutive-ones-iii
# detail: https://leetcode.com/submissions/detail/401377306/
# datetime: Sun Sep 27 20:37:33 2020
# runtime: 644 ms
# memory: 14.5 MB

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i, j, k, n = 0, 0, 0, len(A)
        result = 0
        while j < n:
            if A[j] == 0:
                k += 1
                while k > K:
                    if A[i] == 0:
                        k -= 1
                    i += 1
            result = max(result, j - i + 1)
            j += 1
        return result