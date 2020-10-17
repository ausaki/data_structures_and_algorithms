# title: binary-subarrays-with-sum
# detail: https://leetcode.com/submissions/detail/403916338/
# datetime: Sat Oct  3 21:58:28 2020
# runtime: 236 ms
# memory: 14.8 MB

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        sums = [0] * (len(A) + 1)
        sums[0] = 1
        s = 0
        result = 0
        for a in A:
            s += a
            if s >= S:
                result += sums[s - S]
            sums[s] += 1
        return result