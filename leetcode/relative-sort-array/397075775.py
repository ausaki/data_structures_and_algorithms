# title: relative-sort-array
# detail: https://leetcode.com/submissions/detail/397075775/
# datetime: Thu Sep 17 23:49:59 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        idx = dict(zip(arr2, range(len(arr2))))
        arr1.sort(key=lambda k: (idx.get(k, len(arr2)), k))
        return arr1