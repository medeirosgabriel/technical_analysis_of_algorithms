from queue import PriorityQueue
    
nodes, edges = map(int, input().split())
maxn = nodes + 5
visited_l = [False] * maxn
distance = [[10000000, 10000000] for i in range(maxn)]
adjacency_l = [[] for i in range(maxn)]
    
for i in range(edges):
    v1, v2, dist = map(int, input().split())
    adjacency_l[v1].append((v2, dist))
    adjacency_l[v2].append((v1, dist))
    
def dijsktra(start_node):
    mpq = PriorityQueue()
    distance[start_node][0] = 0
    mpq.put((0, start_node))
    while not mpq.empty():
        dist, node = mpq.get()
        if (node == 1):
            return True
        visited_l[node] = True
        for node_n, dist_s in adjacency_l[node]:
            if not visited_l[node_n] and distance[node_n][0] > distance[node][0] + dist_s:
                distance[node_n][0] = distance[node][0] + dist_s
                distance[node_n][1] = node
                mpq.put((distance[node_n][0], node_n))
    return False
    
found = dijsktra(nodes)
    
if (found):
    print(1, end = ' ')
    node = 1
    while(distance != 10000000):
        if distance[node][1] != 10000000:
            print(distance[node][1], end = ' ')
            node = distance[node][1]
        else:
            break
    print()
else:
    print(-1)