from heapq import heappush, heappop
 
def trace(pre, dest):
	path = []
	while dest != -1:
		path.append(dest)
		dest = pre[dest]
	path.reverse()
	for v in path:
		print(v + 1, end = ' ')
 
def dijkstra(graph):
	n = len(graph)
	INF = int(1e18)
	dist = [INF] * n
	pre = [-1] * n
	heap = [(0, 0)]
	dist[0] = 0
	while len(heap) > 0:
		d, u = heappop(heap)
		if d > dist[u]: 
			continue
		for edge in graph[u]:
			v, w = edge[0], dist[u] + edge[1]
			if w < dist[v]:
				dist[v], pre[v] = w, u
				heappush(heap, (dist[v], v))
 
	if pre[n-1] == -1:
		return False
 
	trace(pre, n-1)
	return True

n,m = map(int,input().split())
g = [[] for _ in range(n)]
 
for _ in range(m):
    u, v, c = list(map(int, input().split()))
    g[u-1].append((v-1, c))
    g[v-1].append((u-1, c))
 
if not dijkstra(g):
    print(-1)