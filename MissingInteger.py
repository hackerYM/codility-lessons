def solution(A):
    
    positive_int = 1
    positive_arr = sorted(num for num in set(A) if num > 0)
    
    for idx, num in enumerate(positive_arr):
        if num != positive_int:
            return idx+1
        positive_int += 1
        
    return positive_int
