# title: delivering-boxes-from-storage-to-ports
# detail: https://leetcode.com/submissions/detail/430149296/
# datetime: Sun Dec 13 15:51:57 2020
# runtime: 2360 ms
# memory: 144.7 MB

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            j = bisect.bisect(prefix_weight, prefix_weight[i] + maxWeight, i + 1, min(i + maxBoxes + 1, n + 1))
            j -= 2
            t = 1 + prefix_ports[j + 1] - prefix_ports[i]
            if i > 0 and boxes[i][0] == boxes[i - 1][0]:
                t += 1
            if j + 1 == n or boxes[j + 1][0] != boxes[j][0]:
                return dp(j + 1) + t
            a = dp(j + 1) + t
            b = 2 * n + 1
            if boxes[j][0] > i:
                b = dp(boxes[j][0]) + (t - 1)
            return min(a, b)
        
        prefix_weight = [0]
        prefix_ports = [0]
        prev_port, prev_idx = -1, -1
        for i, b in enumerate(boxes):
            prefix_weight.append(b[1] + prefix_weight[-1])
            prefix_ports.append((b[0] != prev_port) + prefix_ports[-1])
            if b[0] == prev_port:
                b[0] = prev_idx
            else:
                prev_port, prev_idx = b[0], i
                b[0] = i
        n = len(boxes)
        # print(prefix_weight)
        # print(prefix_ports)
        # print(boxes)
        return dp(0)