# title: sum-of-all-odd-length-subarrays
# detail: https://leetcode.com/submissions/detail/398804006/
# datetime: Tue Sep 22 00:40:41 2020
# runtime: 24 ms
# memory: 13.9 MB

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        n = len(arr)
        for i, a in enumerate(arr):
            # if i % 2 == 0:
            #     le = i // 2 + 1
            #     re = (n - i - 1) // 2
            #     lo = le - 1
            #     ro = (n - i) // 2
            #     s += a * (le * re + le + lo * ro) 
            # else:
            #     lo = i // 2 + 1
            #     ro = (n - i - 1) // 2
            #     le = lo 
            #     re = (n - i) // 2
            #     s += a * (lo * ro + lo + le * re)
            s += a * (i * (n - i) // 2 + (n - i - 1) // 2 + 1)
        return s