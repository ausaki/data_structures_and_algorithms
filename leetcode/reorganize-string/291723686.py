# title: reorganize-string
# detail: https://leetcode.com/submissions/detail/291723686/
# datetime: Mon Jan  6 20:36:32 2020
# runtime: 32 ms
# memory: 12.8 MB

class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt = [(-n, c) for c, n in collections.Counter(S).items()]
        heapq.heapify(cnt)
        s = []
        while len(cnt) >= 2:
            n1, c1 = heapq.heappop(cnt)
            n2, c2 = heapq.heappop(cnt)
            s.append(c1)
            s.append(c2)
            if n1 < -1:
                heapq.heappush(cnt, (n1 + 1, c1))
            if n2 < -1:
                heapq.heappush(cnt, (n2 + 1, c2))
        if cnt:
            n, c = cnt[0]
            if n < -1:
                return ''
            s.append(c)
        return ''.join(s)
        