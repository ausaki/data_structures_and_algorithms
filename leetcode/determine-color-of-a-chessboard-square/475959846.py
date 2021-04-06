# title: determine-color-of-a-chessboard-square
# detail: https://leetcode.com/submissions/detail/475959846/
# datetime: Sun Apr  4 00:03:00 2021
# runtime: 32 ms
# memory: 14.2 MB

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = ord(coordinates[0]) - ord('a'), int(coordinates[1])
        return x % 2 == y % 2
