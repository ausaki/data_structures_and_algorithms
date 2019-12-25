# title: h-index-ii
# detail: https://leetcode.com/submissions/detail/284715689/
# datetime: Mon Dec  9 12:46:22 2019
# runtime: 152 ms
# memory: 19.4 MB

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i, c in enumerate(citations[::-1]):
            if c <= i + 1:
                return max(i, c)
        return len(citations)