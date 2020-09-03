# title: build-an-array-with-stack-operations
# detail: https://leetcode.com/submissions/detail/382294488/
# datetime: Tue Aug 18 01:18:35 2020
# runtime: 24 ms
# memory: 13.9 MB

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        j = 0
        for i in range(1, n + 1):
            ops.append('Push')
            if i < target[j]:
                ops.append('Pop')
            else:
                j += 1
            if j >=  len(target):
                break
        return ops