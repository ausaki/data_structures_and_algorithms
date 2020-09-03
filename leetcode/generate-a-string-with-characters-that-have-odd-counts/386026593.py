# title: generate-a-string-with-characters-that-have-odd-counts
# detail: https://leetcode.com/submissions/detail/386026593/
# datetime: Tue Aug 25 13:48:51 2020
# runtime: 24 ms
# memory: 13.8 MB

class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2:
            return 'a' * n
        return 'a' * (n - 1) + 'b'