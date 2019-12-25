# title: subarray-sum-equals-k
# detail: https://leetcode.com/submissions/detail/287289422/
# datetime: Fri Dec 20 14:58:22 2019
# runtime: 132 ms
# memory: 15.2 MB

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = collections.Counter()
        prefix_sum[0] = 1
        res = 0
        s = 0
        for num in nums:
            s += num
            res += prefix_sum.get(s - k, 0)
            prefix_sum[s] += 1
        return res