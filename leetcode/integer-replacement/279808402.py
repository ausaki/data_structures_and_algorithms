# title: integer-replacement
# detail: https://leetcode.com/submissions/detail/279808402/
# datetime: Mon Nov 18 18:47:13 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    __cache = {}
    def integerReplacement(self, n: int) -> int:
        # if n == 1:
        #     return 0
        # if n in self.__cache:
        #     return self.__cache.get(n)
        # if n & 0x1:
        #     c = 1 + min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))
        #     self.__cache[n] = c
        #     return c
        # c = 1 + self.integerReplacement(n >> 1)
        # self.__cache[n] = c
        # return c
        
        count = 0
        while n > 1:
            if n & 1:
                if n == 3 or (n >> 1) & 1 == 0:
                    n -= 1
                else:
                    n += 1
            else:
                n >>= 1
            count += 1
        return count
        
        