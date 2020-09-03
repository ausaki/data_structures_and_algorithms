# title: number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
# detail: https://leetcode.com/submissions/detail/390349302/
# datetime: Thu Sep  3 14:40:38 2020
# runtime: 684 ms
# memory: 26.4 MB

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k])
        cnt = 1 if s / k >= threshold else 0
        for i in range(k, len(arr)):
            s += -arr[i - k] + arr[i]
            if s / k >= threshold:
                cnt += 1
        return cnt