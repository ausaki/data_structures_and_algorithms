# title: make-array-strictly-increasing
# detail: https://leetcode.com/submissions/detail/396181776/
# datetime: Wed Sep 16 01:22:38 2020
# runtime: 708 ms
# memory: 14.4 MB

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        m, n = len(arr1), len(arr2)
        # arr1.append(10 ** 9 + 1)
        # arr1.insert(0, -1)
        dp = {-1: 0}
        M = 3000
        for a in arr1:
            dp2 = {}
            for b, c in dp.items():
                if a > b:
                    dp2[a] = min(dp2.get(a, M), c)
                i = bisect.bisect(arr2, b)
                if i < n:
                    j = arr2[i]
                    dp2[j] = min(dp2.get(j, M), c + 1)
            dp = dp2
        # print(dp)
        result = min(dp.values(), default=M)
        return result if result < M else -1