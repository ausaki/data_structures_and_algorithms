# title: sum-of-mutated-array-closest-to-target
# detail: https://leetcode.com/submissions/detail/392703489/
# datetime: Tue Sep  8 14:46:43 2020
# runtime: 108 ms
# memory: 14.9 MB

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.append(0)
        arr.sort()
        n = len(arr)
        s0 = 0
        arrsum = []
        for i in range(n):
            s0 += arr[i]
            arrsum.append(s0 + arr[i] * (n - i - 1))
        i = bisect.bisect(arrsum, target)
        if i == n:
            return arr[n - 1]
        d = target - arrsum[i - 1]
        k, r = divmod(d, (n - i))
        if r <= (n - i) - r:
            return arr[i - 1] + k
        return arr[i - 1] + k + 1
        
        