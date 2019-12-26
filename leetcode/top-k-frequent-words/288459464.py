# title: top-k-frequent-words
# detail: https://leetcode.com/submissions/detail/288459464/
# datetime: Wed Dec 25 21:49:31 2019
# runtime: 56 ms
# memory: 12.9 MB

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        items = sorted([[-c, w] for w, c in collections.Counter(words).items()])
        return [items[i][1] for i in range(k)]