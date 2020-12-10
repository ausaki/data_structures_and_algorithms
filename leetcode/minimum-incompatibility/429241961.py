# title: minimum-incompatibility
# detail: https://leetcode.com/submissions/detail/429241961/
# datetime: Thu Dec 10 22:59:32 2020
# runtime: 3432 ms
# memory: 24.1 MB

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        d=len(nums)//k # the length of each partition
        
        @lru_cache(None)
        def helper(nums):
            if not nums:
                return 0
            ret=10**15
            for a in combinations(nums,d): # choose a as a partition
                if len(set(a))<d: # check for duplicates
                    continue
                left=list(nums) # numbers left after removing partition a
                for v in a:
                    left.remove(v)
                ret=min(ret,max(a)-min(a)+helper(tuple(left)))
            return ret
        
        ans=helper(tuple(nums)) # turn the input into a tuple so the function can be cached
        return ans if ans!=10**15 else -1
