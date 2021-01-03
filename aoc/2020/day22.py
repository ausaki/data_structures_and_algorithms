import collections
from functools import lru_cache
import sys
sys.setrecursionlimit(5000)

def solution1(p1, p2):
    p1, p2 = collections.deque(reversed(p1)), collections.deque(reversed(p2))
    while True:
        if not p1:
            return sum(i * c for i, c in enumerate(p2, 1))
        if not p2:
            return sum(i * c for i, c in enumerate(p1, 1))
        c1, c2 = p1.pop(), p2.pop()
        if c1 < c2:
            p2.appendleft(c2)
            p2.appendleft(c1)
        else:
            p1.appendleft(c1)
            p1.appendleft(c2)


def solution2(p1, p2, cache):
    p1, p2 = collections.deque(p1), collections.deque(p2)
    while True:
        if not p1:
            return False, sum(i * c for i, c in enumerate(reversed(p2), 1))
        if not p2:
            return True, sum(i * c for i, c in enumerate(reversed(p1), 1))
        key = (tuple(p1), tuple(p2))
        if key in cache:
            return True, sum(i * c for i, c in enumerate(reversed(p1), 1))
        cache.add(key)
        c1, c2 = p1.popleft(), p2.popleft()
        w = c1 > c2
        if len(p1) >= c1 and len(p2) >= c2:
            w, s = solution2(list(p1)[:c1], list(p2)[:c2], set())
        if w:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
        

def main():
    p1 = []
    p2 = []
    n, m = map(int, input().split())
    for i in range(n):
        p1.append(int(input()))
    for i in range(m):
        p2.append(int(input()))
    # print(solution1(p1, p2))
    print(solution2(tuple(p1), tuple(p2), set()))

main()