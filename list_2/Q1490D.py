def tree(numbers, start, end, out, deep):
	position = separation(numbers, start, end)
	out[position] = deep
	if (position > start): 
		tree(numbers, start, position - 1, out, deep + 1)
	if (position < end): 
		tree(numbers, position + 1, end, out, deep + 1)
		
def separation(numbers, start, end):
	index = start
	max_ = numbers[start]
	for i in range(start + 1, end + 1):
		if (numbers[i] > max_):
			index = i
			max_ = numbers[i]
	return index


n = int(input())

for i in range(n):
	t = int(input())
	out = [-1] * t
	numbers = [int(number) for number in input().split()]
	tree(numbers, 0, len(numbers) - 1, out, 0)
	print(" ".join([str(e) for e in out]))
