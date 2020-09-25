# title: replace-elements-with-greatest-element-on-right-side
# detail: https://leetcode.com/submissions/detail/392670489/
# datetime: Tue Sep  8 13:23:22 2020
# runtime: 128 ms
# memory: 14.9 MB

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], m = m, max(arr[i], m)
        return arr