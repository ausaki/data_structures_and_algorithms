# title: brick-wall
# detail: https://leetcode.com/submissions/detail/287039726/
# datetime: Thu Dec 19 13:21:11 2019
# runtime: 196 ms
# memory: 17.4 MB

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefix_sum = collections.Counter()
        max_cnt = 0
        for row in wall:
            s = 0
            for brick in row[:-1]:
                s += brick
                prefix_sum[s] += 1
                max_cnt = max(max_cnt, prefix_sum[s])
        return len(wall) - max_cnt