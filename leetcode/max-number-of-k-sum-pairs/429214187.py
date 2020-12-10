# title: max-number-of-k-sum-pairs
# detail: https://leetcode.com/submissions/detail/429214187/
# datetime: Thu Dec 10 20:41:23 2020
# runtime: 768 ms
# memory: 27.5 MB

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = collections.Counter()
        res = 0
        for i in nums:
            j = cnt[k - i]
            if j > 0:
                res += 1
                if j == 1:
                    cnt.pop(k - i)
                else:
                    cnt[k - i] = j - 1
            else:
                cnt[i] += 1
        return res