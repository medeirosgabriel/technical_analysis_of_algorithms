n = int(input())
numbers = [int(number) for number in input().split()]

dp = {}
maxi = 0
endi = 0 
endi_index = 0

def solution(numbers, endi, pos):
	if (pos >= 0):
		if(numbers[pos] == endi):
			solution(numbers, endi - 1, pos - 1)
			print(pos + 1, end = " ")
		else:
			solution(numbers, endi, pos - 1)

for i in range(n):
	key = numbers[i] - 1
	if (not key in dp): 
		dp[numbers[i]] = 1
	else:
		dp[numbers[i]] = dp[key] + 1
	if (dp[numbers[i]] > maxi):
		endi_index = i
		endi = numbers[i]
		maxi = dp[numbers[i]]

print(maxi)

solution(numbers, endi-1, endi_index-1)
print(endi_index + 1)
