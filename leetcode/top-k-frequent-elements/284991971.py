# title: top-k-frequent-elements
# detail: https://leetcode.com/submissions/detail/284991971/
# datetime: Tue Dec 10 16:46:34 2019
# runtime: 104 ms
# memory: 17.2 MB

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        uniq = [(c, n) for n, c in cnt.items()]
        hq = uniq[:k]
        heapq.heapify(hq)
        for i in range(k, len(uniq)):
            if uniq[i][0] <= hq[0][0]:
                continue
            heapq.heappushpop(hq, uniq[i])
        return [n for c, n in hq]