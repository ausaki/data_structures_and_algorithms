# title: determine-color-of-a-chessboard-square
# detail: https://leetcode.com/submissions/detail/475914748/
# datetime: Sat Apr  3 22:33:53 2021
# runtime: 36 ms
# memory: 14.3 MB

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = coordinates[0], coordinates[1]
        x = ord(x) - ord('a')
        y = int(y)
        if x % 2:
            return y % 2 == 1
        return y % 2 == 0