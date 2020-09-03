# title: maximum-length-of-repeated-subarray
# detail: https://leetcode.com/submissions/detail/288708834/
# datetime: Thu Dec 26 22:48:28 2019
# runtime: 2756 ms
# memory: 37.8 MB

class Solution(object):
    def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)