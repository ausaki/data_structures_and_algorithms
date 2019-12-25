# title: brick-wall
# detail: https://leetcode.com/submissions/detail/287038987/
# datetime: Thu Dec 19 13:17:23 2019
# runtime: 196 ms
# memory: 17.8 MB

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefix_sum = collections.Counter()
        for row in wall:
            s = 0
            for brick in row[:-1]:
                s += brick
                prefix_sum[s] += 1
        if prefix_sum:
            return len(wall) - prefix_sum.most_common(1)[0][1]
        return len(wall)