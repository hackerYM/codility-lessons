import sys

def solution(A):
    
    min_diff = sys.maxsize
    front_sum, rear_sum = 0, sum(A)
    
    for num in A[:-1]:
        front_sum += num
        rear_sum -= num
        
        if abs(front_sum - rear_sum) < min_diff:
            min_diff = abs(front_sum - rear_sum)
    
    return min_diff
