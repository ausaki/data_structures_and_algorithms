# title: binary-subarrays-with-sum
# detail: https://leetcode.com/submissions/detail/403914589/
# datetime: Sat Oct  3 21:52:03 2020
# runtime: 288 ms
# memory: 17.4 MB

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        sums = collections.Counter([0])
        s = 0
        result = 0
        for a in A:
            s += a
            result += sums[s - S]
            sums[s] += 1
        return result