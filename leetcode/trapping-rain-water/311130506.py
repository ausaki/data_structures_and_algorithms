# title: trapping-rain-water
# detail: https://leetcode.com/submissions/detail/311130506/
# datetime: Tue Mar 10 14:40:07 2020
# runtime: 56 ms
# memory: 13.4 MB

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        N = len(height)
        if N <= 2: return 0
        max_height = 0
        m = -1
        for i, h in enumerate(height):
            if h > max_height:
                max_height = h
                m = i
        i = 0
        while i < m:
            h = height[i]
            k = N
            for j in range(i + 1, m):
                if height[j] < h:
                    total += h - height[j]
                    height[j] = h
                elif height[j] > h and k == N:
                    k = j
            i = k
        i = N - 1
        while i > m:
            h = height[i]
            k = -1
            for j in range(i - 1, m, -1):
                if height[j] < h:
                    total += h - height[j]
                    height[j] = h
                elif height[j] > h and k == -1:
                    k = j
            i = k
        return total