# title: trapping-rain-water
# detail: https://leetcode.com/submissions/detail/311118916/
# datetime: Tue Mar 10 13:57:10 2020
# runtime: 56 ms
# memory: 14.4 MB

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        N = len(height)
        if N <= 2: return 0
        pairs = sorted(zip(height, range(N)), reverse=True)
        left = right = pairs[0][1]
        for h, i in pairs[1:]:
            # print(h, i)
            if i < left:
                total += sum([h - height[j] for j in range(i + 1, left) if height[j] < h])
                left = i
            if i > right:
                total += sum([h - height[j] for j in range(right + 1, i) if height[j] < h])
                right = i
        return total