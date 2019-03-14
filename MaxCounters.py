def solution(N, A):
    
    result = [0] * N
    max_counter = current_max = 0 
    
    for num in A:
        if num <= N:
            if result[num-1] < max_counter:
                result[num-1] = max_counter
            result[num-1] += 1
            
            if result[num-1] > current_max:
                current_max = result[num-1]
        else:
            max_counter = current_max
    
    for idx in range(len(result)):
        if result[idx] < max_counter:
            result[idx] = max_counter
            
    return result
