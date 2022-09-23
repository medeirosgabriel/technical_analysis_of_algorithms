def solution(word, char):
    if (len(word) == 1):
        if(word[0] == chr(char)):
            return 0
        else:
            return 1
    
    fir_h = 0
    sec_h = 0
    size = len(word)
    for i in range(size):
        if (i < int(size/2) and chr(char) != word[i]):
            fir_h += 1
        if (i >= int(size/2) and chr(char) != word[i]):
            sec_h += 1
    
    char += 1
    left = solution(word[0 : int(size/2)], char)
    right = solution(word[int(size/2) : size], char)
    
    return min(
        right + fir_h,
        left + sec_h
    )


tests = int(input())

for t in range(tests):
    size = int(input())
    word = input()
    print(solution(word, ord('a')))