# title: distant-barcodes
# detail: https://leetcode.com/submissions/detail/399700329/
# datetime: Wed Sep 23 23:01:46 2020
# runtime: 580 ms
# memory: 15.9 MB

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        q = [[-v, k] for k, v in collections.Counter(barcodes).items()]
        heapq.heapify(q)
        i = 0
        while q:
            tmp = None
            if i > 0 and barcodes[i - 1] == q[0][1]:
                tmp = heapq.heappop(q)
            item = heapq.heappop(q)
            barcodes[i] = item[1]
            item[0] += 1
            if item[0] < 0:
                heapq.heappush(q, item)
            if tmp:
                heapq.heappush(q, tmp)
            i += 1
        return barcodes