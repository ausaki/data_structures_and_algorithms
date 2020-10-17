# title: 3sum-with-multiplicity
# detail: https://leetcode.com/submissions/detail/404317468/
# datetime: Sun Oct  4 17:04:20 2020
# runtime: 68 ms
# memory: 14.4 MB

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        cnt = collections.Counter(A)
        result = 0
        M = 10 ** 9 + 7
        if target % 3 == 0:
            a = cnt[target // 3]
            result = (result + a * (a - 1) * (a - 2) // 6) % M
        keys = sorted(cnt.keys())
        n = len(keys)
        for i in range(n):
            for j in range(i + 1, n):
                a = target - keys[i] - keys[j]
                if a > keys[j]:
                    result = (result + cnt[keys[i]] * cnt[keys[j]] * cnt[a]) % M
        for i in keys:
            a = target - i * 2
            if a  != i:
                result = (result + cnt[a] * cnt[i] * (cnt[i] - 1) // 2) % M
        return result