# title: arithmetic-subarrays
# detail: https://leetcode.com/submissions/detail/412806663/
# datetime: Sun Oct 25 10:47:12 2020
# runtime: 232 ms
# memory: 14.4 MB

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for s, e in zip(l, r):
            if e - s + 1 <= 2:
                result.append(True)
                continue
            A = sorted(nums[s: e + 1])
            d = A[1] - A[0]
            result.append(all(b - a == d for a, b in zip(A, A[1:])))
        return result