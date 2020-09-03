# title: maximum-number-of-non-overlapping-substrings
# detail: https://leetcode.com/submissions/detail/377461271/
# datetime: Fri Aug  7 22:33:33 2020
# runtime: 80 ms
# memory: 15.3 MB

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        c_range = dict()
        chs = [chr(i) for i in range(97, 123)]

        for c in chs:
            if c in s:
                start = s.index(c)
                end = len(s) - s[::-1].index(c) - 1
                c_range[c] = [start, end]
        for c in c_range:
            while True:
                changed = False
                for cc in chs:
                    if cc != c:
                        start, end = c_range[c]
                        if cc in s[start: end+1]:
                            if c_range[cc][0] < start or c_range[cc][1] > end:
                                c_range[c] = [min(c_range[cc][0], start), max(c_range[cc][1], end)]
                                changed = True
                                break
                if changed:
                    continue
                else:
                    break
        c_range = [c_range[key] for key in c_range]
        
        c_range.sort(key=lambda x:x[1])        
        min_start = -1
        result = []
        while len(c_range):
            start, end = c_range.pop(0)
            if start < min_start:
                continue
            else:
                result.append(s[start:end+1])
                min_start = end + 1
        return result