# title: lexicographical-numbers
# detail: https://leetcode.com/submissions/detail/285253580/
# datetime: Wed Dec 11 21:12:55 2019
# runtime: 172 ms
# memory: 19.7 MB

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def next_num(m):
            k = m * 10
            if k <= n:
                return k
            m += 1
            while m % 10 == 0:
                m //= 10
            while m > n:
                m = m // 10 + 1
                while m % 10 == 0:
                    m //= 10
            return m
        temp = []
        curr = 1
        res.append(curr)
        temp.append((0, 0))
        for i in range(n - 1):
            curr = next_num(curr)
            if curr == 2:
                break
            res.append(curr)
            s = str(curr)
            temp.append((len(s) - 1, int(s[1:])))
        for i in range(2, 10):
            for k, j in temp:
                m = i * (10 ** k) + j
                if m <= n:
                    res.append(m)
        return res
            