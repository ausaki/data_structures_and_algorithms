# title: maximum-number-of-non-overlapping-substrings
# detail: https://leetcode.com/submissions/detail/377467858/
# datetime: Fri Aug  7 22:53:31 2020
# runtime: 184 ms
# memory: 15 MB

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
        ranges = sorted(ranges.values(), key=lambda r: r[1] - r[0])
        indices = []
        result = []
        for start, end in ranges:
            for start_, end_ in indices:
                if start > end_ or end < start_:
                    continue
                else:
                    break
            else:
                indices.append([start, end])
                result.append(s[start: end + 1])
        return result
                    