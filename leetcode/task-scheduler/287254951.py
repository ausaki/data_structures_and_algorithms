# title: task-scheduler
# detail: https://leetcode.com/submissions/detail/287254951/
# datetime: Fri Dec 20 12:01:45 2019
# runtime: 560 ms
# memory: 13.2 MB

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        N = len(tasks)
        tasks = collections.Counter(tasks)
        res = 0
        while tasks:
            _tasks = tasks.most_common(n + 1)
            for t, c in _tasks:
                tasks[t] -= 1
                if tasks[t] == 0:
                    tasks.pop(t)
            res += n + 1 if tasks else len(_tasks)
        return res