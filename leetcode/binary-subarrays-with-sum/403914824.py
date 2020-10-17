# title: binary-subarrays-with-sum
# detail: https://leetcode.com/submissions/detail/403914824/
# datetime: Sat Oct  3 21:52:55 2020
# runtime: 280 ms
# memory: 17.5 MB

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        sums = collections.Counter([0])
        s = 0
        result = 0
        for a in A:
            s += a
            if s >= S:
                result += sums[s - S]
            sums[s] += 1
        return result