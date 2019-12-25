# title: zigzag-conversion
# detail: https://leetcode.com/submissions/detail/283651832/
# datetime: Wed Dec  4 17:13:48 2019
# runtime: 60 ms
# memory: 12.9 MB

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        N = len(s)
        T = 2 * numRows - 2
        if T <= 0:
            return s
        res = [0] * N
        k = 0
        for i in range(numRows):
            j = i
            while j < N:
                # print(k, j, s[j])
                res[k] = s[j]
                k += 1
                m = j % T
                if m < numRows - 1:
                    j += (T - 2 * m) 
                elif m == numRows - 1:
                    j += T
                else:
                    j += 2 * (T - m)
        return ''.join(res)