# title: least-number-of-unique-integers-after-k-removals
# detail: https://leetcode.com/submissions/detail/380670307/
# datetime: Fri Aug 14 14:34:43 2020
# runtime: 484 ms
# memory: 32.9 MB

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = sorted(collections.Counter(arr).items(), key=lambda a: a[1])
        n = len(cnt)
        for i in range(n):
            if k < cnt[i][1]:
                return n - i
            k -= cnt[i][1]
        return 0
            