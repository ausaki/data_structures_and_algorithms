import random

n = 10
m = 0
edges = set()
lines = ['?\n']
for j in range(10):
    for i in range(5):
        u = random.randint(1, n)
        v = random.randint(1, n)
        while v == u:
            v = random.randint(1, n)
        if u > v:
            u, v = v, u
        edge = (u, v)
        if edge in edges:
            continue
        edges.add((u, v))
        lines.append('+ {} {}\n'.format(u, v))
    for i in range(2):
        edge = edges.pop()
        lines.append('- {} {}\n'.format(*edge))
    lines.append('?\n')

with open('connect.in', 'w') as fp:
    fp.write('{} {}\n'.format(n, len(lines)))
    fp.writelines(lines)


