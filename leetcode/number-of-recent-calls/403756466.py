# title: number-of-recent-calls
# detail: https://leetcode.com/submissions/detail/403756466/
# datetime: Sat Oct  3 11:42:18 2020
# runtime: 276 ms
# memory: 18.7 MB

class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        t -= 3000
        while self.q and self.q[0] < t:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)