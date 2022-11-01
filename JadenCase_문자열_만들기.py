def solution(s):
    stringArray = list(map(lambda x: x.lower(), s.split(" ")))
    
    result = list(map(lambda x: x.capitalize(), stringArray))
    
    return " ".join(result)