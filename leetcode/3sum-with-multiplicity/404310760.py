# title: 3sum-with-multiplicity
# detail: https://leetcode.com/submissions/detail/404310760/
# datetime: Sun Oct  4 16:38:00 2020
# runtime: 556 ms
# memory: 14.1 MB

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        cnt1 = [0] * 101
        cnt2 = [0] * 101
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