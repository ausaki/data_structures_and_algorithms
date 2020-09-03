# title: maximum-number-of-non-overlapping-substrings
# detail: https://leetcode.com/submissions/detail/377474547/
# datetime: Fri Aug  7 23:14:38 2020
# runtime: 304 ms
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
            s_set = set(s[start + 1: end])
            q = collections.deque(s_set)
            while q:
                start_, end_ = ranges[q.popleft()]
                if start_ < start:
                    start = start_
                if end_ > end:
                    new_set = set(s[end + 1: end_]) - s_set
                    q.extend(new_set)
                    s_set.update(new_set)
                    end = end_
            ranges[char] = [start, end]
        ranges = sorted(ranges.values(), key=lambda r: r[1])
        result = []
        last_end = -1
        for start, end in ranges:
            if start > last_end:
                result.append(s[start: end + 1])
                last_end = end
        return result
                    