class FenwickTree:
    def __init__(self, data) -> None:
        self.bit = None
        self._build(data)
    
    def _build(self, data):
        n = len(data) + 1
        self.bit = [0] * n
        for i in range(1, n):
            for j in range(i, i & (i - 1), -1):
                self.bit[i] += data[j - 1]
    
    def add(self, i, delta):
        i += 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i
    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i &= i - 1
        return s

    def range_sum(self, l, r):
        return self.sum(r + 1) - self.sum(l)


data = list(range(10))
ft = FenwickTree(data)
print(data)
print(ft.bit)
print(ft.sum(5))
print(ft.sum(9))
print(ft.add(2, 5))
print(ft.sum(3))