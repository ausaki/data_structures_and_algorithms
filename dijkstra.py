def dijkstra():
    costs = [10000] * N
    costs[K - 1] = 0
    queue = [(0, K)]
    seen = set()
    graph = collections.defaultdict(dict)
    for u, v, w in times:
        graph[u][v] = w
    while queue:
        t1, i = heapq.heappop(queue)
        if i in seen:
            continue
        seen.add(i)
        costs[i - 1] = t1
        for j, t2 in graph[i].items():
            if j in seen:
                continue
            heapq.heappush(queue, (t1 + t2, j))
    m = max(costs)
    return m if m != 10000 else -1