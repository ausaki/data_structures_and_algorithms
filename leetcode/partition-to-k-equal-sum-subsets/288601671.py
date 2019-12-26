# title: partition-to-k-equal-sum-subsets
# detail: https://leetcode.com/submissions/detail/288601671/
# datetime: Thu Dec 26 11:41:49 2019
# runtime: 1748 ms
# memory: 12.8 MB

from functools import lru_cache
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # @lru_cache(None)
        def partition(subs, i):
            if i == -1:
                return all([i == s for i in subs])
            for j in range(k):
                if subs[j] + nums[i] <= s:
                    subs[j] += nums[i]
                    if partition(subs, i - 1):
                        return True
                    subs[j] -= nums[i]
            return False
        
        subs = [0] * k
        N = len(nums)
        nums.sort()
        S = sum(nums)
        if S % k: return False
        s = S // k
        return partition(subs, N - 1)