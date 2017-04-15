def solution(s):
    result = []
    while s:
        result.append(s[:2]) if len(s) >= 2 else result.append(s[0]+"_")
        s = s[2:]
    return result
