def dijkstra(graph, start, target):
    n = len(graph) # # of vertices
    q = [(0, start)]
    dist = [math.inf] * n
    dist[start] = 0
    while q:
        w, u = heapq.heappop(q)
        if w > dist[u]:
            continue
        if u == target:
            break
        for v, w2 in graph[u]:
            w2 += w
            if w2 < dist[v]:
                heapq.heappush(q, (w2, v))
                dist[v] = w2