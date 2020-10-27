import bisect

class FenwickTree:
    def __init__(self, n, data=None) -> None:
        self.bit = [0] * (n + 1)
        if data is not None:
            self._build(data)
    
    def _build(self, data):
        for i in range(1, len(self.bit)):
            self.bit[i] = sum(data[j - 1] for j in range(i, i & (i - 1), -1))
    
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
        return self.sum(r) - self.sum(l - 1)

def solution(n):
    cards = list(range(n))
    ft = FenwickTree(n)
    i = 0 # curr index
    w = 0
    for j in range(1, n + 1):
        l, r = 0, n - 1
        threshold = (j + 1) % (n - j + 1)
        if threshold == 0:
            threshold = n - j + 1
        while l <= r:
            m = (l + r) // 2
            k = (i + m) % n
            removed = ft.range_sum(i, k) if k >= i else j - ft.range_sum(k + 1, i - 1) - 1
            t = m + 1 - removed
            if t < threshold:
                l = m + 1
            else:
                r = m - 1
        # print(i, l)
        i = (i + l) % n
        ft.add(i, 1)
        cards[i] = j
        i = (i + 1) % n
    # print(w)
    return cards

def check(cards):
    import collections
    q = collections.deque(cards)
    for i in range(len(cards)):
        for j in range(i + 1):
            q.append(q.popleft())
        print(q.popleft(), end=' ')
    
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        cards = solution(n)
        print(' '.join(map(str, cards)))
main()