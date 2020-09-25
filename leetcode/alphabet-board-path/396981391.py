# title: alphabet-board-path
# detail: https://leetcode.com/submissions/detail/396981391/
# datetime: Thu Sep 17 17:49:17 2020
# runtime: 36 ms
# memory: 14 MB

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        m, n = 6, 5
        result = []
        i, j = 0, 0
        for c in target:
            c = ord(c) - ord('a')
            if c == i * n + j:
                result += '!'
                continue
            ii, jj = divmod(c, n)
            if ii > i:
                result += ['L', 'R'][j < jj] * abs(j - jj)
                result += ['U', 'D'][i < ii] * abs(i - ii)
            else:
                result += ['U', 'D'][i < ii] * abs(i - ii)
                result += ['L', 'R'][j < jj] * abs(j - jj)
            i, j = ii, jj
            result += '!'
        return result