# title: crawler-log-folder
# detail: https://leetcode.com/submissions/detail/409427931/
# datetime: Fri Oct 16 19:22:53 2020
# runtime: 48 ms
# memory: 14.5 MB

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == './':
                continue
            if log == '../':
                depth = max(depth - 1, 0)
            else:
                depth += 1
        return depth