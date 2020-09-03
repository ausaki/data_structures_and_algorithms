# title: global-and-local-inversions
# detail: https://leetcode.com/submissions/detail/288942186/
# datetime: Fri Dec 27 18:55:39 2019
# runtime: 388 ms
# memory: 13.4 MB

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N = len(A)
        stack = []
        i = 0
        while i < N:
            j = i + 1
            while j < N and A[j] > A[j - 1]:
                stack.append(A[j - 1])
                j += 1
            if j == N:
                break
            stack.append(A[j - 1])
            i = j
            if len(stack) > 1 and A[i] < stack[-2]:
                return False
            if i + 1 < N and (A[i] > A[i + 1] or A[i + 1] < stack[-1]):
                return False
            i += 1
        return True