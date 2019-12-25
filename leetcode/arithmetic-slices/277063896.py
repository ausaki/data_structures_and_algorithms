# title: arithmetic-slices
# detail: https://leetcode.com/submissions/detail/277063896/
# datetime: Fri Nov  8 22:36:43 2019
# runtime: 32 ms
# memory: 12.8 MB

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # reutrn self._by_dp(A)
        return self._by_math(A)
        
    def _by_dp(self, A):
        '''time: O(n^2) space: O(n^2)'''
        N = len(A)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        count = 0
        for i in reversed(range(N - 2)):
            for j in range(i + 2, N):
                if j == i + 2:
                    if A[j] - A[j - 1] == A[j - 1] - A[j - 2]:
                        dp[i][j] = 1
                        count += 1
                else:
                    if dp[i + 1][j] and A[i + 1] - A[i] == A[i + 2] - A[i + 1]:
                        dp[i][j] = 1
                        count += 1
        return count
    
    def _by_math(self, A):
        '''time: O(n) space: O(1)'''
        i = 0
        N = len(A)
        count = 0
        while i < N - 2:
            diff = A[i + 1] - A[i]
            length = 2
            j = i + 2
            while j < N and A[j] - A[j - 1] == diff:
                length += 1
                j += 1
            if length >= 3:
                count += (length - 2) * (length - 2 + 1) // 2
            i = j - 1
        return count
                
        
        