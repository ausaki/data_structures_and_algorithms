# title: queue-reconstruction-by-height
# detail: https://leetcode.com/submissions/detail/285478021/
# datetime: Thu Dec 12 21:11:05 2019
# runtime: 100 ms
# memory: 13.1 MB

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key=lambda p: (-p[0], p[1]))
        for p in people:
            res.insert(p[1], p)
        return res