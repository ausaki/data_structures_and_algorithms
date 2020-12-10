# title: get-maximum-in-generated-array
# detail: https://leetcode.com/submissions/detail/418033301/
# datetime: Sun Nov  8 16:31:04 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        arr = [0, 1]
        ans = 1
        for i in range(2, n + 1):
            arr.append(arr[i // 2] + (arr[i // 2 + 1] if i % 2 else 0))
            ans = max(ans, arr[-1])
        return ans