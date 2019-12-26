# title: top-k-frequent-words
# detail: https://leetcode.com/submissions/detail/288459599/
# datetime: Wed Dec 25 21:50:31 2019
# runtime: 52 ms
# memory: 12.9 MB

import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        items = [[-c, w] for w, c in collections.Counter(words).items()]
        return [item[1] for item in heapq.nsmallest(k, items)]