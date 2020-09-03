# title: three-consecutive-odds
# detail: https://leetcode.com/submissions/detail/384743559/
# datetime: Sun Aug 23 01:24:58 2020
# runtime: 92 ms
# memory: 14.1 MB

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        a, b = arr[0] % 2, arr[1] % 2
        for i in range(2, n):
            c = arr[i] % 2
            if a + b + c == 3:
                return True
            a, b = b, c
        return False