# title: maximum-length-of-pair-chain
# detail: https://leetcode.com/submissions/detail/287742528/
# datetime: Sun Dec 22 20:23:41 2019
# runtime: 228 ms
# memory: 13.1 MB

import operator
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=operator.itemgetter(1, 0))
        res = 0
        a, b = float('-inf'), float('-inf')
        for c, d  in pairs:
            if c > b:
                res += 1
                a, b = c, d
        return res
            