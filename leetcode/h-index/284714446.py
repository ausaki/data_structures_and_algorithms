# title: h-index
# detail: https://leetcode.com/submissions/detail/284714446/
# datetime: Mon Dec  9 12:40:20 2019
# runtime: 28 ms
# memory: 12.8 MB

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c <= i + 1:
                return max(i, c)
        return len(citations)
                