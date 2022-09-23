z, n, m = [int(x) for x in input().split()]

adj = []
vis = []

for i in range(15):
    adj.append([])
    vis.append([])
    for j in range(15):
        adj[i].append([""] * 15)
        vis[i].append([False] * 15)

for i in range(1, z + 1):
    input()
    for j in range(1, n + 1):
        c = list(input())
        for l in range(1, len(c) + 1):
            adj[i][j][l] = c[l - 1]
input()

x, y = [int(e) for e in input().split()]

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def dfs(l, x, y, z, dx, dy, dz):
    if (adj[l][x][y] == '#'):
        return
    
    vis[l][x][y] = True
    
    for i in range(6):
        c = l + dz[i]
        a = x + dx[i]
        b = y + dy[i]
        if (a > 0 and b > 0 and c > 0 and c <= z and a <= n and b <= m and not vis[c][a][b]):
            dfs(c, a, b, z, dx, dy, dz)

dfs(1, x, y, z, dx, dy, dz)

out = 0
for i in range(1, z + 1):
    for j in range(1, n + 1):
        for l in range(1, m + 1):
            if (vis[i][j][l]):
                out += 1

print(out)