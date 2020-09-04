def bfs(i, n):
    q = [(0, i)]
    dist = [float('inf')] * n
    visited = {i}
    while q:
        w, j = heapq.heappop(q)
        if w > dist[j]:
            continue
        visited.add(j)
        for k, w_ in g[j]:
            d = w + w_
            if k not in visited and d < dist[k]:
                heapq.heappush(q, (d, k))
                dist[k] = d