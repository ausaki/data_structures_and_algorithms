# title: the-k-strongest-values-in-an-array
# detail: https://leetcode.com/submissions/detail/381113974/
# datetime: Sat Aug 15 15:04:19 2020
# runtime: 1048 ms
# memory: 27.5 MB

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = (n - 1) // 2
        median = arr[m]
        print(m, median)
        l, r = 0, n - 1
        result = []
        while k > 0 and l <= r:
            if arr[r] - median >= median - arr[l]:
                result.append(arr[r])
                r -= 1
            else:
                result.append(arr[l])
                l += 1
            k -= 1
        return result
