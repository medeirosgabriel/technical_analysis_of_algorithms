from queue import PriorityQueue
    
nodes, edges = map(int, input().split())
maxn = nodes + 5

adjacency_l = [[] for i in range(maxn)]
distance = [10000000 for i in range(maxn)]
par = [False] * maxn
visited_l = [False] * maxn

    
for i in range(edges):
    v1, v2, dist = map(int, input().split())
    adjacency_l[v1].append((v2, dist))
    adjacency_l[v2].append((v1, dist))
    
def dijsktra(start_node, end_node):
    mpq = PriorityQueue()
    mpq.put((0, start_node))
    distance[start_node] = 0
    par[start_node] = -1

    while not mpq.empty():
        dist, node = mpq.get()
        if (node == end_node):
            return True
        visited_l[node] = True

        for node_n, dist_s in adjacency_l[node]:
            if not visited_l[node_n] and distance[node_n] > distance[node] + dist_s:
                distance[node_n] = distance[node] + dist_s
                mpq.put((distance[node_n], node_n))
                par[node_n] = node
    return False
    
found = dijsktra(1, nodes)
    
if (found):
    path = []

    v = nodes
    while (v != -1):
        path.append(v)
        v = par[v]

    for index in range(len(path) - 1, -1, -1):
        print(path[index], end = " ")
        
    print()

else:
    print(-1)