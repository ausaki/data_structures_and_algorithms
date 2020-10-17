# title: maximize-distance-to-closest-person
# detail: https://leetcode.com/submissions/detail/407879702/
# datetime: Tue Oct 13 02:03:28 2020
# runtime: 124 ms
# memory: 14.6 MB

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i = -1
        result = 0
        for j, s in enumerate(seats):
            if s == 1:
                result = max(result, (j + i) // 2 - i)
                if i == -1:
                    result = max(result, j)
                i = j
        return max(result, len(seats) - 1 - i)