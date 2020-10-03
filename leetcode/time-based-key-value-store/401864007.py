# title: time-based-key-value-store
# detail: https://leetcode.com/submissions/detail/401864007/
# datetime: Tue Sep 29 00:26:21 2020
# runtime: 708 ms
# memory: 70.9 MB

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ''
        l = self.data[key]
        i = bisect.bisect(l, [timestamp + 1])
        if i == 0:
            return ''
        return l[i - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)