# title: number-of-students-doing-homework-at-a-given-time
# detail: https://leetcode.com/submissions/detail/381756903/
# datetime: Sun Aug 16 23:13:40 2020
# runtime: 40 ms
# memory: 13.9 MB

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                cnt += 1
        return cnt