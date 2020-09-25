# title: online-majority-element-in-subarray
# detail: https://leetcode.com/submissions/detail/396598571/
# datetime: Wed Sep 16 22:53:04 2020
# runtime: 1496 ms
# memory: 21.6 MB

class MajorityChecker:

    def __init__(self, A):
        a2i = collections.defaultdict(list)
        for i, x in enumerate(A):
            a2i[x].append(i)
        self.A, self.a2i = A, a2i

    def query(self, left, right, threshold):
        for _ in range(20):
            a = self.A[random.randint(left, right)]
            l = bisect.bisect_left(self.a2i[a], left)
            r = bisect.bisect_right(self.a2i[a], right)
            if r - l >= threshold:
                return a
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)