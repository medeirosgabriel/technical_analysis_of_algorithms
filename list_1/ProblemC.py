tests = int(input())

for i in range(tests):
    n, steps = map(int, input().split())
    florest = [int(n) for n in input().split()]
    if (steps <= n):
        sum_ = 0
        for j in range(steps):
            sum_ += florest[j]
        result = sum_
        for j in range(steps, n, 1):
            sum_ += florest[j]
            sum_ -= florest[j - steps]
            result = max(result, sum_)
        
        result += (steps*(steps-1))/2
        print(int(result))
    else:
        result = (n*(steps-n)) + ((n*(n-1))/2)
        for j in range(n):
            result += florest[j]
        print(int(result))
