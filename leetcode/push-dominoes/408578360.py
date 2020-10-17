# title: push-dominoes
# detail: https://leetcode.com/submissions/detail/408578360/
# datetime: Wed Oct 14 16:38:22 2020
# runtime: 120 ms
# memory: 15.7 MB

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        i, k = -1, -1
        n = len(dominoes)
        result = list(dominoes)
        for j in range(n):
            if dominoes[j] != '.':
                i = j
                continue
            if k < j:
                k = j + 1
                while k < n and dominoes[k] == '.':
                    k += 1
            if i == -1 or dominoes[i] == 'L':
                if k < n and dominoes[k] == 'L':
                    result[j] = 'L'
            else:
                if k >= n or dominoes[k] == 'R':
                    result[j] = 'R'
                else:
                    if k - j < j - i:
                        result[j] = 'L'
                    elif k - j > j - i:
                        result[j] = 'R'
        return ''.join(result)