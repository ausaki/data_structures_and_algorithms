# title: integer-replacement
# detail: https://leetcode.com/submissions/detail/279805151/
# datetime: Mon Nov 18 18:11:11 2019
# runtime: 24 ms
# memory: 12.7 MB

class Solution:
    __cache = {}
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n in self.__cache:
            return self.__cache.get(n)
        if n & 0x1:
            c = 1 + min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))
            self.__cache[n] = c
            return c
        c = 1 + self.integerReplacement(n >> 1)
        self.__cache[n] = c
        return c
        
        