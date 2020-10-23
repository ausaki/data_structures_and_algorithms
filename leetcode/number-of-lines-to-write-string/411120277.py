# title: number-of-lines-to-write-string
# detail: https://leetcode.com/submissions/detail/411120277/
# datetime: Wed Oct 21 01:22:04 2020
# runtime: 28 ms
# memory: 14 MB

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines = 1
        left = 100
        for c in S:
            w = widths[ord(c) - 97]
            if w <= left:
                left -= w
            else:
                lines += 1
                left = 100 - w
        return [lines, 100 - left]