# title: mean-of-array-after-removing-some-elements
# detail: https://leetcode.com/submissions/detail/410256240/
# datetime: Sun Oct 18 22:47:16 2020
# runtime: 52 ms
# memory: 14.3 MB

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        return sum(sorted(arr)[len(arr) * 5 // 100: -len(arr) * 5 // 100]) / (len(arr) * 90 // 100)