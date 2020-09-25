# title: circular-permutation-in-binary-representation
# detail: https://leetcode.com/submissions/detail/394620659/
# datetime: Sat Sep 12 22:33:50 2020
# runtime: 220 ms
# memory: 21.8 MB

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def gray_code(n):
            if n == 1:
                return [0, 1]
            code = gray_code(n - 1)
            code.extend(reversed(code))
            for i in range(1 << (n - 1), 1 << n):
                code[i] |= 1 << (n - 1)
            return code
        
        p = [0, 1]
        m = 1
        while m < n:
            for i in reversed(range(len(p))):
                p.append(p[i] | (1 << m))
            m += 1
        i = p.index(start)
        return p[i:] + p[:i]