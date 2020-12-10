# title: jewels-and-stones
# detail: https://leetcode.com/submissions/detail/412583977/
# datetime: Sat Oct 24 21:22:12 2020
# runtime: 28 ms
# memory: 14 MB

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        return sum(1 for c in S if c in J)