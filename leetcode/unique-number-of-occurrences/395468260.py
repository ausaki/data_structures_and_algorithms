# title: unique-number-of-occurrences
# detail: https://leetcode.com/submissions/detail/395468260/
# datetime: Mon Sep 14 14:25:56 2020
# runtime: 52 ms
# memory: 14.2 MB

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        v = collections.Counter(arr).values()
        return len(set(v)) == len(v)