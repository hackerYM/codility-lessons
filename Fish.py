def solution(A, B):
    
    downstream_fish_stack = []
    survival_count = 0
    
    for idx in range(0, len(A)):
        
        if B[idx] == 1:
            downstream_fish_stack.append(A[idx])
            survival_count += 1
        
        else:
            while downstream_fish_stack and A[idx] > downstream_fish_stack[-1]:
                downstream_fish_stack.pop()
                survival_count -= 1
                
            if not downstream_fish_stack:  # All downstream fishes are eaten.
                survival_count += 1
        
        # print(downstream_fish_stack, survival_count)
        
    return survival_count
