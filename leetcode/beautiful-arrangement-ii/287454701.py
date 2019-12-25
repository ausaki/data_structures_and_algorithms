# title: beautiful-arrangement-ii
# detail: https://leetcode.com/submissions/detail/287454701/
# datetime: Sat Dec 21 11:33:26 2019
# runtime: 44 ms
# memory: 13.8 MB

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        i = 1
        j = n
        m = k // 2
        for i in range(1, m + 1):
            res.append(i)
            res.append(n + 1 - i)
        l = range(m + 1, n + 1 - m)
        if k % 2:
            res.extend(l)
        else:
            res.extend(reversed(l))
        
        return res