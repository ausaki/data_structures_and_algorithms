# title: maximum-number-of-non-overlapping-substrings
# detail: https://leetcode.com/submissions/detail/377442465/
# datetime: Fri Aug  7 21:29:17 2020
# runtime: 4484 ms
# memory: 15.3 MB

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
        print(ranges)
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
                    