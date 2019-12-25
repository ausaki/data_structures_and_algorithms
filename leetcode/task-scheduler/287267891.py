# title: task-scheduler
# detail: https://leetcode.com/submissions/detail/287267891/
# datetime: Fri Dec 20 13:09:48 2019
# runtime: 596 ms
# memory: 13 MB

import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        N = len(tasks)
        tasks = sorted([[c, t] for t, c in collections.Counter(tasks).items()])
        res = 0
        while tasks:
            new_tasks = []
            k = len(tasks)
            for i in range(min(n + 1, k)):
                c, t = tasks.pop()
                c -= 1
                if c > 0:
                    new_tasks.append([c, t])
            
            tasks = list(heapq.merge(tasks, reversed(new_tasks)))
            res += n + 1 if tasks else k
        return res