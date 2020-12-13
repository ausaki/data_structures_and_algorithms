# title: count-the-number-of-consistent-strings
# detail: https://leetcode.com/submissions/detail/429863556/
# datetime: Sat Dec 12 22:35:17 2020
# runtime: 308 ms
# memory: 16.3 MB

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(set(w).issubset(allowed) for w in words)