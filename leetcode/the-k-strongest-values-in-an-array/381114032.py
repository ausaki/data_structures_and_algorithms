# title: the-k-strongest-values-in-an-array
# detail: https://leetcode.com/submissions/detail/381114032/
# datetime: Sat Aug 15 15:04:29 2020
# runtime: 992 ms
# memory: 27.6 MB

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = (n - 1) // 2
        median = arr[m]
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
