# title: task-scheduler
# detail: https://leetcode.com/submissions/detail/287271807/
# datetime: Fri Dec 20 13:31:03 2019
# runtime: 584 ms
# memory: 13 MB

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = list(collections.Counter(tasks).values())
        tasks.sort(reverse=True)
        N = len(tasks)
        res = 0
        while tasks[0]:
            for i in range(n + 1):
                if tasks[0] == 0:
                    break
                if i < N and tasks[i] > 0:
                    tasks[i] -= 1
                res += 1
            tasks.sort(reverse=True)
        return res