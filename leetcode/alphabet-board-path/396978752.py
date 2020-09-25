# title: alphabet-board-path
# detail: https://leetcode.com/submissions/detail/396978752/
# datetime: Thu Sep 17 17:37:29 2020
# runtime: 24 ms
# memory: 13.8 MB

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        m, n = 6, 5
        result = []
        i, j = 0, 0
        for c in target:
            c = ord(c) - ord('a')
            if c == i * n + j:
                result.append('!')
            else:
                ii, jj = divmod(c, n)
                if c == 25:
                    result.append('L' * j + 'D' * (ii - i))
                elif i * n + j == 25:
                    result.append('U' * (i - ii) + 'R' * jj)
                else:
                    if i > ii:
                        result.append('U' * (i - ii))
                    else:
                        result.append('D' * (ii - i))
                    if j > jj:
                        result.append('L' * (j - jj))
                    else:
                        result.append('R' * (jj - j))
                i, j = ii, jj
                result.append('!')
        return ''.join(result)