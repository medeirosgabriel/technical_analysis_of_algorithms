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

def dfs(l, x, y, z):
    if (x > 0 and y > 0 and l > 0 and l <= z and x <= n and y <= m and not vis[l][x][y]):
        if (adj[l][x][y] == '#'):
            return
        vis[l][x][y] = True
        dfs(l + 1, x, y, z)
        dfs(l - 1, x, y, z)
        dfs(l, x + 1, y, z)
        dfs(l, x - 1, y, z)
        dfs(l, x, y + 1, z)
        dfs(l, x, y - 1, z)

dfs(1, x, y, z)

out = 0
for i in range(1, z + 1):
    for j in range(1, n + 1):
        for l in range(1, m + 1):
            if (vis[i][j][l]):
                out += 1

print(out)