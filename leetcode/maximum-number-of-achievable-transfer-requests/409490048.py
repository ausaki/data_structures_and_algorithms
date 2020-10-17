# title: maximum-number-of-achievable-transfer-requests
# detail: https://leetcode.com/submissions/detail/409490048/
# datetime: Fri Oct 16 23:44:24 2020
# runtime: 5288 ms
# memory: 14.1 MB

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        nr = len(requests)
        res = 0

        def test(mask):
            outd = [0] * n
            ind = [0] * n
            for k in range(nr):
                if (1 << k) & mask:
                    outd[requests[k][0]] += 1
                    ind[requests[k][1]] += 1
            return sum(outd) if outd == ind else 0

        for i in range(1 << nr):
            res = max(res, test(i))
        return res