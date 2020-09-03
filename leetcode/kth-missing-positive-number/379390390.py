# title: kth-missing-positive-number
# detail: https://leetcode.com/submissions/detail/379390390/
# datetime: Tue Aug 11 22:48:07 2020
# runtime: 52 ms
# memory: 14 MB

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0
        for i in arr:
            if i > prev + 1:
                k -= i - prev - 1
                if k <= 0:
                    return i + k - 1
            prev = i
        return i + k
                        