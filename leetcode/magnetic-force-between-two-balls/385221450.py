# title: magnetic-force-between-two-balls
# detail: https://leetcode.com/submissions/detail/385221450/
# datetime: Sun Aug 23 23:58:53 2020
# runtime: 3484 ms
# memory: 27.1 MB

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
        
        l, r = 0, position[-1] - position[0]
        while l <= r:
            mid = (l + r) // 2
            c = count(mid)
            if c >= m:
                l = mid + 1
            else:
                r = mid - 1
        return r