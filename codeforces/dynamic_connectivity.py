class DisjSet:
    def __init__(self, n ):
        self.disj_set = [-1] * n
        self._components = n
        self.stack = []

    def find(self, x):
        while self.disj_set[x] >= 0:
            x = self.disj_set[x]
        return x
    
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return -1
        self._components -= 1
        self.stack.append((i, self.disj_set[i], j, self.disj_set[j]))
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
            return i
        if self.disj_set[i] == self.disj_set[j]:
            self.disj_set[j] -= 1
        self.disj_set[i] = j
        return j
    
    def rollback(self, n):
        for _ in range(n):
            if not self.stack:
                break
            i, iv, j, jv = self.stack.pop()
            self._components += 1
            self.disj_set[i] = iv
            self.disj_set[j] = jv

class SegmentTreeWithArray:

    def __init__(self, n, m) -> None:
        self.size = m
        self.tree = [[] for i in range(4 * self.size)]
        self.result = []
        self.disjset = DisjSet(n)

    def _dfs(self, index, start, end, q):
        ops = 0
        for u, v in self.tree[index]:
            s = self.disjset.union(u, v)
            if s != -1:
                ops += 1
        if start == end:
            if start in q:
                u, v = q[start]
                self.result.append(self.disjset.find(u) == self.disjset.find(v))
        else:
            mid = (start + end) // 2
            self._dfs(2 * index + 1, start, mid, q)
            self._dfs(2 * index + 2, mid + 1, end, q)
        self.disjset.rollback(ops)
    
    def solve(self, q):
        self._dfs(0, 0, self.size - 1, q)
        return self.result

    def _add_query(self, index, start, end, l, r, query):
        if l > r:
            return
        if start == l and end == r:
            self.tree[index].append(query)
            return
        mid  = (start + end) // 2
        self._add_query(2 * index + 1, start, mid, l, min(r, mid), query)
        self._add_query(2 * index + 2, mid + 1, end, max(l, mid + 1), r, query)

    def add_query(self, l, r, query):
        self._add_query(0, 0, self.size - 1, l, r, query)

def main():
    n, m = map(int, input().split())
    if m == 0:
        return
    sgt = SegmentTreeWithArray(n, m)
    g = {}
    q = {}
    for i in range(m):
        op, u, v = map(int, input().split())
        u -= 1
        v -= 1
        if u > v:
            u, v = v, u
        edge = (u, v)
        if op == 0:
            g[edge] = i
        elif op == 1:
            j = g.pop(edge)
            sgt.add_query(j, i - 1, edge)
        else:
            q[i] = edge
    for edge, i in g.items():
        sgt.add_query(i, m - 1, edge)
    result = sgt.solve(q)
    # with open('connect.out', 'w') as fp2:
    #     for i in q:
    #         fp2.write('{}\n'.format(result[i]))
    print('\n'.join('Y' if f else 'N' for f in result))

main()
                

