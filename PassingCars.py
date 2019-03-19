def solution(A):
    
    west_count = len([car for car in A if car == 1])
    passing_count = 0
    
    for car in A:
        if car == 1:
            west_count -= 1
        else:
            passing_count += west_count
    
        if passing_count > 1000000000:
            return -1
        
    return passing_count
