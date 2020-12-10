# title: max-number-of-k-sum-pairs
# detail: https://leetcode.com/submissions/detail/429217489/
# datetime: Thu Dec 10 21:00:42 2020
# runtime: 648 ms
# memory: 27.5 MB

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = collections.Counter(nums)
        res = 0
        while cnt:
            a, b = cnt.popitem()
            if a + a == k:
                res += b // 2
            else:
                c = cnt.pop(k - a, 0)
                res += min(b, c)
        return res