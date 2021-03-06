# title: snapshot-array
# detail: https://leetcode.com/submissions/detail/396937530/
# datetime: Thu Sep 17 15:09:26 2020
# runtime: 684 ms
# memory: 35.1 MB

class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.snapid = 0
        self.data = collections.defaultdict(list)

    def set(self, index: int, val: int) -> None:
        d = self.data[index]
        if not d or d[-1][0] != self.snapid:
            d.append([self.snapid, val])
        else:
            d[-1][1] = val

    def snap(self) -> int:
        self.snapid += 1
        return self.snapid - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.data:
            d = self.data[index]
            i = bisect.bisect(d, [snap_id, -1])
            if i == len(d):
                return d[-1][1]
            if d[i][0] == snap_id:
                return d[i][1]
            if i > 0:
                return d[i - 1][1]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)