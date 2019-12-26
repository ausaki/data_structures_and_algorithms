# title: partition-to-k-equal-sum-subsets
# detail: https://leetcode.com/submissions/detail/288608165/
# datetime: Thu Dec 26 12:13:43 2019
# runtime: 1640 ms
# memory: 12.8 MB

class Solution(object):
    # def canPartitionKSubsets(self, nums, k):
    def canPartitionKSubsets(self, A, k):
        if len(A) < k:
            return False
        ASum = sum(A)
        A.sort(reverse=True)
        if ASum % k != 0:
            return False
        target = [ASum / k] * k

        def dfs(pos):
            if pos == len(A): return True
            for i in range(k):
                if target[i] >= A[pos]:
                    target[i] -= A[pos]
                    if dfs(pos + 1):
                        return True
                    target[i] += A[pos]
            return False
        return dfs(0)