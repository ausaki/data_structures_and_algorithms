# title: alphabet-board-path
# detail: https://leetcode.com/submissions/detail/396980121/
# datetime: Thu Sep 17 17:43:38 2020
# runtime: 40 ms
# memory: 14 MB

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        m, n = 6, 5
        result = []
        i, j = 0, 0
        for c in target:
            c = ord(c) - ord('a')
            if c == i * n + j:
                result.append('!')
                continue
            ii, jj = divmod(c, n)
            if c == 25:
                result.append('L' * j + 'D' * (ii - i))
            elif i * n + j == 25:
                result.append('U' * (i - ii) + 'R' * jj)
            else:
                result.append(['U', 'D'][i < ii] * abs(i - ii))
                result.append(['L', 'R'][j < jj] * abs(j - jj))
            i, j = ii, jj
            result.append('!')
        return ''.join(result)