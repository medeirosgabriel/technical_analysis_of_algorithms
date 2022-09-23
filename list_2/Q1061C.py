n = int(input())
numbers = [int(number) for number in input().split()]

size = max(numbers) + 1
dp = [0] * size
matrix = []
out = 0
mod = int(1e9 + 7)

dp[0] = 1

for i in range(size):
	matrix.append([])

for i in range(1, size, 1):
	for j in range(i, size, i):
		matrix[j].append(i)

for x in numbers:
	for i in range(len(matrix[x]) - 1, -1, -1):
		curr = matrix[x][i]
		out = (out + dp[curr- 1]) % mod
		dp[curr] = (dp[curr - 1] + dp[curr]) % mod

print(out)
