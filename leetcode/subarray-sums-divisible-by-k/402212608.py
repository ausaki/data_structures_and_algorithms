# title: subarray-sums-divisible-by-k
# detail: https://leetcode.com/submissions/detail/402212608/
# datetime: Tue Sep 29 18:37:36 2020
# runtime: 288 ms
# memory: 18 MB

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        rems = [0] * K
        rems[0] += 1
        r = 0
        result = 0
        for a in A:
            r = (r + a) % K
            result += rems[r]
            rems[r] += 1
        return result