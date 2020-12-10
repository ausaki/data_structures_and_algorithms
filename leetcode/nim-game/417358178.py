# title: nim-game
# detail: https://leetcode.com/submissions/detail/417358178/
# datetime: Fri Nov  6 16:12:48 2020
# runtime: 28 ms
# memory: 14 MB

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0