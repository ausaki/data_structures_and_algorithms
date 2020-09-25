# title: sum-of-mutated-array-closest-to-target
# detail: https://leetcode.com/submissions/detail/392690313/
# datetime: Tue Sep  8 14:12:20 2020
# runtime: 96 ms
# memory: 14.7 MB

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.append(0)
        arr.sort()
        n = len(arr)
        diff = 1e6
        s0 = 0
        f = False
        for i in range(n - 1):
            s0 += arr[i]
            s1 = s0 + arr[i] * (n - i - 1)
            for j in range(arr[i + 1] - arr[i]):
                d = abs(s1 - target)
                if d < diff:
                    diff = d
                    value = arr[i] + j  
                if s1 > target and d > diff:
                    f = True
                    break
                s1 += n - i - 1
            if f:
                break
        if f:
            return value
        s0 += arr[n - 1]
        if abs(s0 - target) < diff:
            value = arr[n - 1]
        return value