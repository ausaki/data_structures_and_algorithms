# title: partition-labels
# detail: https://leetcode.com/submissions/detail/291727444/
# datetime: Mon Jan  6 21:04:37 2020
# runtime: 28 ms
# memory: 12.8 MB

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans