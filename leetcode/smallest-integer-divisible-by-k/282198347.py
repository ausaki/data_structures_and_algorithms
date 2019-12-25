# title: smallest-integer-divisible-by-k
# detail: https://leetcode.com/submissions/detail/282198347/
# datetime: Thu Nov 28 12:00:17 2019
# runtime: 52 ms
# memory: 16.9 MB

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # d = K % 10
        # if d not in (1, 3, 7, 9):
        #     return -1
        # N = 0
        # if d == 1:
        #     N = K * 1
        # elif d == 3:
        #     N = K * 7
        # elif d == 7:
        #     N = K * 3
        # else:
        #     N = K * 9
        # i = 2
        # while i < len(str(N)):
        #     for j in range(0, 10):
        #         t = N + (K * j) + 10 ** (i - 1)
        #         s = t // (10 ** (i - 1))
        #         r = s % 10
        #         if r == 1:
        #             N = t
        #             i += 1
        #             break
        #     else:
        #         return False
        # if K % 10 not in {1, 3, 7, 9}: return -1
        mod, mod_set = 0, set()
        for length in range(1, K + 1):
            mod = (10 * mod + 1) % K
            if mod == 0: return length
            if mod in mod_set: return -1
            mod_set.add(mod)
        return -1