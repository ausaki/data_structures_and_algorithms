# title: range-sum-of-sorted-subarray-sums
# detail: https://leetcode.com/submissions/detail/377927822/
# datetime: Sat Aug  8 23:38:29 2020
# runtime: 788 ms
# memory: 13.8 MB

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pq = [(x, i) for i, x in enumerate(nums)]
        ans = 0
        heapq.heapify(pq)
        
        for k in range(1, right+1):
            x, i = heappop(pq)
            if k >= left: ans += x
            if i + 1 < len(nums):
                heappush(pq, (x + nums[i+1], i+1))
    
        return ans % 1_000_000_007