# title: number-of-equivalent-domino-pairs
# detail: https://leetcode.com/submissions/detail/397023791/
# datetime: Thu Sep 17 21:01:40 2020
# runtime: 280 ms
# memory: 23.3 MB

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(v * (v - 1) // 2 for k, v in collections.Counter(min(a, b) *  10 + max(a, b) for a, b in dominoes).items())
