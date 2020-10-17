# title: sort-array-by-parity-ii
# detail: https://leetcode.com/submissions/detail/404304367/
# datetime: Sun Oct  4 16:14:19 2020
# runtime: 200 ms
# memory: 16.2 MB

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i = -1
        for j, a in enumerate(A):
            if a % 2:
                if A[i + 1] % 2 == 0:
                    A[i + 2], A[j] = a, A[i + 2]
                    i += 2
            else:
                if A[i + 1] % 2 == 1:
                    A[i + 1], A[j] = a, A[i + 1]
                    if A[i + 2] % 2:
                        i += 2
        return A
                    
        