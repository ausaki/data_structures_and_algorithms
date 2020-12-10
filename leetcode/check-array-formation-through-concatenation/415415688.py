# title: check-array-formation-through-concatenation
# detail: https://leetcode.com/submissions/detail/415415688/
# datetime: Sun Nov  1 10:37:56 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        pos = {a: i for i, a in enumerate(arr)}
        for p in pieces:
            i = pos.get(p[0], -1)
            if i == -1:
                return False
            for j in range(len(p)):
                if i + j >= n or arr[i + j] != p[j]:
                    return False
        return True