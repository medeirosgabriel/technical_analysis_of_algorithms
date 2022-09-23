x0, y0, x1, y1 = map(int, input().split())
n = int(input())

allow = {}
distance = {}
    
for i in range(n):
    r, c1, c2 = map(int, input().split())
    if (r in allow):
        allow[r].append((c1, c2))
    else:
        allow[r] = []
        allow[r].append((c1, c2))
    
my_queue = []
mx = [-1, -1, -1, 1, 1, 1, 0, 0]
my = [-1, 0, 1, -1, 0, 1, 1, -1]
    
def bfs(x0, y0):
    distance[(x0, y0)] = 0
    my_queue.append((x0, y0))
    while my_queue:
        xc, yc = my_queue.pop(0)
        for i in range(len(mx)):
            x = xc + mx[i]
            y = yc + my[i]
            if (allow.get(x) != None):
                for c1, c2 in allow[x]:
                    if (y >= c1 and y <= c2):
                        if (distance.get((x, y)) == None or distance[(x, y)] > distance[(xc, yc)] + 1):
                            distance[(x, y)] = distance[(xc, yc)] + 1
                            my_queue.append((x, y))
                        break

bfs(x0, y0)
    
if (distance.get((x1, y1)) != None ):
    print(distance[x1, y1])
else:
    print(-1)