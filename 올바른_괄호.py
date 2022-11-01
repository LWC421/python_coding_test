def solution(s):
    splitted = list(s)
    stack = []
    
    for c in splitted:
        if len(stack) == 0:
            if c == ")":
                return False
            stack.append(c)
            continue
            
        source = stack[-1]
        if(isValid(source, c)):
            stack.pop()
        else:
            stack.append(source)
        
    
    if len(stack) != 0:
        return False

    return True

def isValid(source, target):
    if source=="(" and target==")":
        return True
    
    return False