def solution(s):
    count = 0
    answer = 0
    
    while(s != "1"):
        tmp = s.replace("0", "")
        removed = len(s) - len(tmp)
        answer += removed
        count += 1
        s = str(format(len(tmp), "b"))

    
    return [count, answer]

