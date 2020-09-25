# title: sum-of-all-odd-length-subarrays
# detail: https://leetcode.com/submissions/detail/398792775/
# datetime: Tue Sep 22 00:06:57 2020
# runtime: 40 ms
# memory: 14.1 MB

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        n = len(arr)
        for i, a in enumerate(arr):
            print(i, a)
            if i % 2 == 0:
                le = i // 2 + 1
                re = (n - i - 1) // 2
                lo = le - 1
                ro = (n - i) // 2
                # print(le, re, lo, ro)
                s += a * (le * re + le + lo * ro) 
            else:
                lo = (i - 1) // 2 + 1
                ro = (n - i - 1) // 2
                le = lo 
                re = (n - i) // 2
                # print(lo, ro, le, re)
                s += a * (lo * ro + lo + le * re)
        return s