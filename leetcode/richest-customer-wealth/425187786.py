# title: richest-customer-wealth
# detail: https://leetcode.com/submissions/detail/425187786/
# datetime: Sun Nov 29 10:32:28 2020
# runtime: 112 ms
# memory: 14.4 MB

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))