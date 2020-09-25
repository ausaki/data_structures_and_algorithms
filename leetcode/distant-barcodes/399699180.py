# title: distant-barcodes
# detail: https://leetcode.com/submissions/detail/399699180/
# datetime: Wed Sep 23 22:58:19 2020
# runtime: 588 ms
# memory: 15.9 MB

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        q = [[-v, k] for k, v in collections.Counter(barcodes).items()]
        heapq.heapify(q)
        result = []
        while q:
            if result and result[-1] == q[0][1]:
                tmp = heapq.heappop(q)
                item = heapq.heappop(q)
                result.append(item[1])
                item[0] += 1
                if item[0] < 0:
                    heapq.heappush(q, item)
                heapq.heappush(q, tmp)
            else:
                item = heapq.heappop(q)
                result.append(item[1])
                item[0] += 1
                if item[0] < 0:
                    heapq.heappush(q, item)
        return result