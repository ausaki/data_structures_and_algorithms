# title: duplicate-zeros
# detail: https://leetcode.com/submissions/detail/397726116/
# datetime: Sat Sep 19 13:35:57 2020
# runtime: 76 ms
# memory: 14.6 MB

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        for i in range(n):
            arr[i] |= ((arr[i - 1] >> 4 if i else 0) + (arr[i] == 0)) << 4
        for i in range(n - 1, -1, -1):
            a = arr[i] & 0x0f
            j = (arr[i] >> 4) - (a == 0)
            if i + j < n:
                arr[i + j] = a
            if a == 0 and i + j + 1 < n:
                arr[i + j + 1] = a
