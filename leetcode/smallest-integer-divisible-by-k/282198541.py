# title: smallest-integer-divisible-by-k
# detail: https://leetcode.com/submissions/detail/282198541/
# datetime: Thu Nov 28 12:01:30 2019
# runtime: 36 ms
# memory: 12.7 MB

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 10 not in {1, 3, 7, 9}: return -1
        mod = 0
        for length in range(1, K + 1):
            mod = (10 * mod + 1) % K
            if mod == 0: return length
        return -1