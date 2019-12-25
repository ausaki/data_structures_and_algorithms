# title: adding-two-negabinary-numbers
# detail: https://leetcode.com/submissions/detail/282947205/
# datetime: Sun Dec  1 22:39:09 2019
# runtime: 64 ms
# memory: 12.8 MB

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        N = len(arr1)
        M = len(arr2)
        i = N - 1
        j = M - 1
        s = 0
        res = []
        while i >= 0 or j >= 0:
            if (N - i - 1) % 2:
                # odd
                n = (-arr1[i] if i >= 0 else 0) + (-arr2[j] if j >= 0 else 0) + s
                if n <= 0:
                    s, n = divmod(-n, 2)
                    s = -s
                elif n == 1:
                    n = 1
                    s = 1
                res.append(n)
            else:
                # even
                n = (arr1[i] if i >= 0 else 0) + (arr2[j] if j >= 0 else 0) + s
                s, n = divmod(n, 2)
                res.append(n)
            i -= 1
            j -= 1
        print(s)
        print(res[::-1])
        if s != 0:
            k = len(res) % 2
            res.append(1)
            if (k == 1 and s == 1) or (k == 0 and s == -1):
                res.append(1)
        res = res[::-1]
        while res and res[0] == 0:
            res.pop(0)
        return res if res else [0]