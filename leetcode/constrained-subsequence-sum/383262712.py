# title: constrained-subsequence-sum
# detail: https://leetcode.com/submissions/detail/383262712/
# datetime: Wed Aug 19 23:51:09 2020
# runtime: 836 ms
# memory: 33.4 MB

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = [(-nums[0], 0)]
        result = nums[0]
        for i in range(1, n):
            while heap and heap[0][1] < i - k:
                heapq.heappop(heap)
            a = -heap[0][0]
            m = nums[i] + (a if a > 0 else 0)
            heapq.heappush(heap, (-m, i))
            result = max(result, m)
        return result