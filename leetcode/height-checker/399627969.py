# title: height-checker
# detail: https://leetcode.com/submissions/detail/399627969/
# datetime: Wed Sep 23 18:18:12 2020
# runtime: 24 ms
# memory: 13.7 MB

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 if h1 != h2 else 0 for h1, h2 in zip(sorted(heights), heights))