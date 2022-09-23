from heapq import heappush, heappop
 
def dijkstra(adj):
    n = len(adj)
    INF = int(1e18)
    dist = [INF] * n
    pre = [-1] * n
    heap = [(0, 0)]
    dist[0] = 0
    while len(heap) > 0:
        d, u = heappop(heap)
        if d > dist[u]: 
            continue
        for edge in adj[u]:
            v, w = edge[0], dist[u] + edge[1]
            if w < dist[v]:
                dist[v], pre[v] = w, u
                heappush(heap, (dist[v], v))
                
    if pre[n - 1] == -1:
        print(-1)
    else:
        path = []
        target = n - 1
        while target != -1:
            path.append(target)
            target = pre[target]
        path.reverse()
        for v in path:
            print(v + 1, end = ' ')


vertices, edges = map(int,input().split())
adj = [[] for _ in range(vertices)]

for _ in range(edges):
    v1, v2, distance = list(map(int, input().split()))
    adj[v1 - 1].append((v2 - 1, distance))
    adj[v2 - 1].append((v1 - 1, distance))
 
dijkstra(adj)
