def solution(n):
    result = 0
    for number in range(1, n+1):
        if(n % number == 0 and number%2 == 1):
            result += 1
    

    return result
