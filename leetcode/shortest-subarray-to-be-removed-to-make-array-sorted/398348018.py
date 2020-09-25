# title: shortest-subarray-to-be-removed-to-make-array-sorted
# detail: https://leetcode.com/submissions/detail/398348018/
# datetime: Sun Sep 20 23:36:18 2020
# runtime: 732 ms
# memory: 28.6 MB

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        j, k = -1, -1
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                if j == -1:
                    j = i
                k = i
        if j == -1:
            return 0
        k += 1
        if arr[j] <= arr[k]:
            return k - j - 1
        result = 10 ** 9
        l = n
        for i in range(j, -1, -1):
            l = bisect.bisect_left(arr, arr[i], k, l)
            result = min(result, l - i - 1)
        result = min(result, k)
        return result
            
        