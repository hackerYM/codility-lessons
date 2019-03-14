def solution(X, A):
    
    num_set = set()
    
    for idx, num in enumerate(A):
        num_set.add(num)
        if len(num_set) == X:
            return idx
    
    return -1
