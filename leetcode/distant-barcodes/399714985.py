# title: distant-barcodes
# detail: https://leetcode.com/submissions/detail/399714985/
# datetime: Wed Sep 23 23:46:09 2020
# runtime: 448 ms
# memory: 15.8 MB

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n, i = len(barcodes), 0
        for k, v in collections.Counter(barcodes).most_common():
            for _ in range(v):
                barcodes[i] = k
                i += 2
                if i >= n:
                    i = 1
        return barcodes
