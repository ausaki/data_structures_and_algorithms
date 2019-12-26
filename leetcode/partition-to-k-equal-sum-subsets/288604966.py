# title: partition-to-k-equal-sum-subsets
# detail: https://leetcode.com/submissions/detail/288604966/
# datetime: Thu Dec 26 11:58:04 2019
# runtime: 48 ms
# memory: 13.7 MB

from functools import lru_cache
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def partition(subs, i):
            if i == -1:
                return True
            key = tuple(sorted(subs))
            if i in cache and key in cache[i]:
                return cache[i][key]
            for j in range(k):
                if subs[j] + nums[i] <= s:
                    subs[j] += nums[i]
                    if partition(subs, i - 1):
                        return True
                    subs[j] -= nums[i]
            cache[i][key] = False
            return False
        
        cache = collections.defaultdict(dict)
        subs = [0] * k
        N = len(nums)
        nums.sort()
        S = sum(nums)
        if S % k: return False
        s = S // k
        return partition(subs, N - 1)