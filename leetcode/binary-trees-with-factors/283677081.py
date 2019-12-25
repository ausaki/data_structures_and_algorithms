# title: binary-trees-with-factors
# detail: https://leetcode.com/submissions/detail/283677081/
# datetime: Wed Dec  4 21:15:06 2019
# runtime: 424 ms
# memory: 12.9 MB

class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        index = {n: i for i, n in enumerate(A)}
        dp = [1] * len(A)
        
        for i, n in enumerate(A):
            for j in range(i):
                if n % A[j] == 0:
                    m = n // A[j]
                    if m in index:
                        dp[i] += (dp[j] * dp[index[m]]) % (10 ** 9 + 7)
        return sum(dp) % (10 ** 9 + 7)
