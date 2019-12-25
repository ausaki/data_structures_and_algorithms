# title: task-scheduler
# detail: https://leetcode.com/submissions/detail/287274715/
# datetime: Fri Dec 20 13:46:39 2019
# runtime: 408 ms
# memory: 13.1 MB

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = list(collections.Counter(tasks).values())
        tasks.sort(reverse=True)
        N = len(tasks)
        res = 0
        max_val = tasks[0] - 1
        idle = max_val * n
        for i in range(1, N):
            idle -= min(tasks[i], max_val)
        return idle + sum(tasks) if idle > 0 else sum(tasks)