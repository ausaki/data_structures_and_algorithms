# title: pancake-sorting
# detail: https://leetcode.com/submissions/detail/402303296/
# datetime: Wed Sep 30 00:15:52 2020
# runtime: 44 ms
# memory: 14.2 MB

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for v in range(n, 0, -1):
            i = arr.index(v, n - v)
            if i > 0:
                result.append(i)
            result.append(i + 1)
            k = arr[i]
            for j in range(i - 1, -1, -1):
                arr[j + 1] = arr[j]
            arr[0] = arr[i]
        return result            