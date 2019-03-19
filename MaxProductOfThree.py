def solution(A):
    
    A.sort()
    
    max_value = A[-1] * A[-2] * A[-3]
    if A[0] * A[1] * A[-1] > max_value:
        max_value = A[0] * A[1] * A[-1]
    
    return max_value
