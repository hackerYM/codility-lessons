def solution(A):
    
    for idx, num in enumerate(sorted(A)):
        if idx+1 != num:
            return 0
            
    return 1
