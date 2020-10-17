# title: maximum-number-of-achievable-transfer-requests
# detail: https://leetcode.com/submissions/detail/409463324/
# datetime: Fri Oct 16 22:10:14 2020
# runtime: 5388 ms
# memory: 14 MB

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        result = 0
        for i in range(1 << m):
            net = [0] * n
            k = 0
            for j in range(m):
                if (i >> j) & 1:
                    f, t = requests[j]
                    net[f] -= 1
                    net[t] += 1
                    k += 1
            if all(i == 0 for i in net):
                result = max(result, k)
        return result