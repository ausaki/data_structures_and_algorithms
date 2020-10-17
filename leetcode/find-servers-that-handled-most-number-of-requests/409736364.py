# title: find-servers-that-handled-most-number-of-requests
# detail: https://leetcode.com/submissions/detail/409736364/
# datetime: Sat Oct 17 15:30:00 2020
# runtime: 1628 ms
# memory: 34.6 MB

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        q = []
        available_servers = list(range(k))
        cnt = [0] * k
        for i, (s, t) in enumerate(zip(arrival, load)):
            while q and q[0][0] <= s:
                _, server = heapq.heappop(q)
                bisect.insort(available_servers, server)
            if not available_servers:
                continue
            i = i % k
            j = bisect.bisect_left(available_servers, i)
            if j == len(available_servers):
                j = 0
            server = available_servers.pop(j)
            heapq.heappush(q, (s + t, server))
            cnt[server] += 1
        result = []
        max_ = 0
        for i, j in enumerate(cnt):
            if j > max_:
                max_ = j
                result = [i]
            elif j == max_:
                result.append(i)
        return result