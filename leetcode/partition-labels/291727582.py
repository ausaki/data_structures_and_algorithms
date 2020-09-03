# title: partition-labels
# detail: https://leetcode.com/submissions/detail/291727582/
# datetime: Mon Jan  6 21:05:45 2020
# runtime: 32 ms
# memory: 12.6 MB

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        pos = collections.defaultdict(int)
        for i, c in enumerate(S):
            pos[c] = i
        partitions = []
        j = -1
        k = -1
        for i, c in enumerate(S):
            if pos[c] > k:
                k = pos[c]
            if i == k:
                partitions.append(i - j)
                j = i
        return partitions