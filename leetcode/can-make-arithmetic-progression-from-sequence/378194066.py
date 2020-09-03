# title: can-make-arithmetic-progression-from-sequence
# detail: https://leetcode.com/submissions/detail/378194066/
# datetime: Sun Aug  9 11:23:08 2020
# runtime: 44 ms
# memory: 14.2 MB

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] == diff:
                continue
            return False
        return True