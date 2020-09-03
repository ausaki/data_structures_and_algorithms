# title: range-sum-of-sorted-subarray-sums
# detail: https://leetcode.com/submissions/detail/377921144/
# datetime: Sat Aug  8 23:27:55 2020
# runtime: 644 ms
# memory: 14.3 MB

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        def gen(i):
            s = 0
            for j in range(i, n):
                s += nums[j]
                yield s
                
        it = heapq.merge(*[gen(i) for i in range(n)])
        for i in range(left - 1):
            next(it)
        result = 0
        M = 10 ** 9 + 7
        for i in range(left - 1, right):
            result = (result + next(it)) % M
        return result