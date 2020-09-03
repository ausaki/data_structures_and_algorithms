# title: maximum-number-of-non-overlapping-substrings
# detail: https://leetcode.com/submissions/detail/377469154/
# datetime: Fri Aug  7 22:57:39 2020
# runtime: 180 ms
# memory: 14.9 MB

import string

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
            while True:
                start, end = ranges[char]
                ss = s[start: end + 1]
                for ch in string.ascii_lowercase:
                    if ch == char:
                        continue
                    if ch in ss:
                        start_, end_ = ranges[ch]
                        if start_ < start or end_ > end:
                            ranges[char] = [min(start, start_), max(end, end_)]
                            break
                else:
                    break
        ranges = sorted(ranges.values(), key=lambda r: r[1])
        result = []
        last_end = -1
        for start, end in ranges:
            if start > last_end:
                result.append(s[start: end + 1])
                last_end = end
        return result
                    