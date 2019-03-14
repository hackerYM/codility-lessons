def solution(A):
    
    N = len(A) + 1
    num_sum = (1 + N) * N // 2
    
    return num_sum - sum(A)
