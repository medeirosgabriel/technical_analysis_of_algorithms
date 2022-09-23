n = int(input())
numbers = [int(number) for number in input().split()]

dp = {}
maxi = 0
endi = 0 
endi_index = 0

if (n == 1):
	print(1)
else:
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

	out = []
	x = endi - 1
	pos = endi_index - 1
	while (pos >= 0):
		if(numbers[pos] == x):
			out = [str(pos + 1)] + out
			x -= 1
			pos -= 1
		else:
			pos -= 1

	out += [str(endi_index + 1)]
	print(" ".join(out))
		
