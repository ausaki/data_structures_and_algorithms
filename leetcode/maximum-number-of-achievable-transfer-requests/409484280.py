# title: maximum-number-of-achievable-transfer-requests
# detail: https://leetcode.com/submissions/detail/409484280/
# datetime: Fri Oct 16 23:25:01 2020
# runtime: 2004 ms
# memory: 14.2 MB

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        requests = [[f, t] for f, t in requests if f != t]
        self_loop = m - len(requests)
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
        return result + self_loop