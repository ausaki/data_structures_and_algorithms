# title: longest-happy-string
# detail: https://leetcode.com/submissions/detail/384140347/
# datetime: Fri Aug 21 17:52:31 2020
# runtime: 24 ms
# memory: 13.8 MB

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = []
        chars = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            chars.sort()
            p = s[-1] if s else ''
            for i in range(2, -1, -1):
                if chars[i][1] != p and chars[i][0] != 0:
                    s.append(chars[i][1])
                    chars[i][0] -= 1
                    break
            else:
                break
        result = ''
        counter = {j: i for i, j in chars}
        for c in s:
            if counter[c] != 0:
                result += c * 2
                counter[c] -= 1
            else:
                result += c
        return result
