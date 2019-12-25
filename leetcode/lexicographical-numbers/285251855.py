# title: lexicographical-numbers
# detail: https://leetcode.com/submissions/detail/285251855/
# datetime: Wed Dec 11 20:56:26 2019
# runtime: 132 ms
# memory: 20.9 MB

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def next_num(m):
            for i in range(0, 10):
                k = m * 10 + i
                if k <= n:
                    res.append(k)
                    next_num(k)
                else:
                    break
        for i in range(1, 10):
            if i <= n:
                res.append(i)
            next_num(i)
        # def next_num(m):
        #     k = m * 10
        #     if k <= n:
        #         return k
        #     m += 1
        #     while m % 10 == 0:
        #         m //= 10
        #     while m > n:
        #         m = m // 10 + 1
        #         while m % 10 == 0:
        #             m //= 10
        #     return m
        # curr = 1
        # res.append(curr)
        # for i in range(n - 1):
        #     curr = next_num(curr)
        #     res.append(curr)
        return res
            