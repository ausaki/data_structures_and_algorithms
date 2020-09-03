# title: maximum-number-of-non-overlapping-substrings
# detail: https://leetcode.com/submissions/detail/377470908/
# datetime: Fri Aug  7 23:03:12 2020
# runtime: 4496 ms
# memory: 15.2 MB

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        ranges = {}
        n = len(s)
        for i, c in enumerate(s):
            if c not in ranges:
                ranges[c] = [i, i]
            else:
                ranges[c][1] = i
        chars = sorted(ranges.keys(), key=lambda k: ranges[k][0])
        for char in chars:
            start, end = ranges[char]
            i = start + 1
            while i < end:
                start_, end_ = ranges[s[i]]
                start = min(start, start_)
                end = max(end, end_)
                i += 1
            ranges[char] = [start, end]
        ranges = sorted(ranges.values(), key=lambda r: r[1])
        result = []
        last_end = -1
        for start, end in ranges:
            if start > last_end:
                result.append(s[start: end + 1])
                last_end = end
        return result
                    