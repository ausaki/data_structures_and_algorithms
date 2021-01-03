# title: minimum-operations-to-make-a-subsequence
# detail: https://leetcode.com/submissions/detail/437850784/
# datetime: Sun Jan  3 12:40:53 2021
# runtime: 4732 ms
# memory: 38.7 MB

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        pos = {a: i for i, a in enumerate(target)}
        n = len(target)
        idx = []
        for i, a in enumerate(arr):
            j = pos.get(a, -1)
            if j >= 0:
                idx.append(j)
        
        lis = [-1]
        for i in idx:
            j = 0
            for j in range(len(lis) - 1, -1, -1):
                if i > lis[j]:
                    break
            if j + 1 == len(lis):
                lis.append(i)
            else:
                lis[j + 1] = i
        return n - len(lis) + 1
            