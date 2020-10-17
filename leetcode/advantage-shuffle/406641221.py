# title: advantage-shuffle
# detail: https://leetcode.com/submissions/detail/406641221/
# datetime: Sat Oct 10 02:18:49 2020
# runtime: 324 ms
# memory: 16.5 MB

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        A.sort()
        idx = sorted(range(n), key=B.__getitem__)
        result = [0] * n
        i = 0
        t = n - 1
        for j, k in enumerate(idx):
            while i < n and A[i] <= B[k]:
                result[idx[t]] = A[i]
                i += 1
                t -= 1
            if i == n:
                break
            result[k] = A[i]
            i += 1
        return result