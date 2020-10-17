# title: 3sum-with-multiplicity
# detail: https://leetcode.com/submissions/detail/404310970/
# datetime: Sun Oct  4 16:38:47 2020
# runtime: 524 ms
# memory: 14.4 MB

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        m = max(A)
        cnt1 = [0] * (m + 1)
        cnt2 = [0] * (m + 1)
        result = 0
        M = 10 ** 9 + 7
        for a in A:
            cnt2[a] += 1
        for a in A:
            cnt2[a] -= 1
            for i, j in enumerate(cnt1):
                if j == 0:
                    continue
                k = target - i - a
                if 0 <= k < len(cnt2) and cnt2[k]:
                    result = (result + j * cnt2[k]) % M
            cnt1[a] += 1
        return result