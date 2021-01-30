# title: tuple-with-same-product
# detail: https://leetcode.com/submissions/detail/443915530/
# datetime: Sun Jan 17 10:47:07 2021
# runtime: 868 ms
# memory: 42.9 MB

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnt = collections.Counter()
        for a, b in itertools.combinations(nums, 2):
            cnt[a * b] += 1
        res = 0
        for k, v in cnt.items():
            res += 8 * v * (v - 1) // 2
        return res