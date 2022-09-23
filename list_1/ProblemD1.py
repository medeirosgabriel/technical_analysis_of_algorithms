from queue import PriorityQueue
    
x0, y0, x1, y1 = map(int, input().split())
n = int(input())

allow = {}
adj = {}
distance = {}
visited = {}
    
mx = [-1, -1, -1, 1, 1, 1, 0, 0]
my = [-1, 0, 1, -1, 0, 1, 1, -1]

allow[(x0, y0)] = True
allow[(x1, y1)] = True
    
for i in range(n):
    r, c1, c2 = map(int, input().split())
    for c in range(c1, c2 + 1):
        allow[(r, c)] = True
        adj[(r, c)] = []
        distance[(r, c)] = 10000000000
        for m in range(len(mx)):
            s1 = my[m]
            s2 = mx[m]
            if ((r + s1, c + s2) in allow):
                adj[(r,c)].append((r + s1, c + s2, 1))
                adj[(r + s1, c + s2)].append((r, c, 1))
                distance[(r + s1, c + s2)] = 10000000000
    
my_priority_queue = PriorityQueue()
    
def bfs(x0, y0):
    distance[(x0, y0)] = 0
    my_priority_queue.put((0, x0, y0))
    while not my_priority_queue.empty():
        dist, xc, yc = my_priority_queue.get()
        if distance[(xc, yc)] < dist:
            continue
        for xn, yn, dist in adj[(xc, yc)]:
            if (xn, yn) in allow and distance[(xn, yn)] > distance[(xc, yc)] + 1:
                distance[(xn, yn)] = distance[(xc, yc)] + 1
                my_priority_queue.put((distance[(xn, yn)], xn, yn))
    
    
bfs(x0, y0)
    
if ((x1, y1) in distance and distance[(x1, y1)] < 10000000000):
    print(distance[x1, y1])
else:
    print(-1)