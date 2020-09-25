# title: alphabet-board-path
# detail: https://leetcode.com/submissions/detail/396981084/
# datetime: Thu Sep 17 17:47:51 2020
# runtime: 28 ms
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
            if ii > i:
                result.append(['L', 'R'][j < jj] * abs(j - jj))
                result.append(['U', 'D'][i < ii] * abs(i - ii))
            else:
                result.append(['U', 'D'][i < ii] * abs(i - ii))
                result.append(['L', 'R'][j < jj] * abs(j - jj))
            i, j = ii, jj
            result.append('!')
        return ''.join(result)