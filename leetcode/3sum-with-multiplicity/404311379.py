# title: 3sum-with-multiplicity
# detail: https://leetcode.com/submissions/detail/404311379/
# datetime: Sun Oct  4 16:40:24 2020
# runtime: 472 ms
# memory: 14.1 MB

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        cnt1 = collections.Counter()
        cnt2 = collections.Counter()
        result = 0
        M = 10 ** 9 + 7
        for a in A:
            cnt2[a] += 1
        for a in A:
            cnt2[a] -= 1
            if cnt2[a] == 0:
                cnt2.pop(a)
            for i, j in cnt1.items():
                k = target - i - a
                result = (result + j * cnt2[k]) % M
            cnt1[a] += 1
        return result