# title: maximum-number-of-achievable-transfer-requests
# detail: https://leetcode.com/submissions/detail/409489449/
# datetime: Fri Oct 16 23:42:24 2020
# runtime: 700 ms
# memory: 14.2 MB

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        requests = [[f, t] for f, t in requests if f != t]
        self_loop, m = m - len(requests), len(requests)
        net = [0] * n
        max_req = 0
        def dfs(i, req):
            nonlocal max_req
            if i == m:
                if all(i == 0 for i in net):
                    max_req = max(max_req, req)
                return
            dfs(i + 1, req)
            f, t = requests[i]
            # keep_going = True
            # if net[f] - 1 < 0 and sum(1 for j in range(i + 1, m) if requests[j][1] == f) + net[f] - 1 < 0:
            #     keep_going = False
            # if not keep_going:
            #     return
            # if net[t] + 1 > 0 and sum(1 for j in range(i + 1, m) if requests[j][0] == t) - net[t] - 1 < 0:
            #     keep_going = False
            # if not keep_going:
            #     return
            net[f] -= 1
            net[t] += 1
            dfs(i + 1, req + 1)
            net[f] += 1
            net[t] -= 1
        dfs(0, 0)
        return max_req + self_loop