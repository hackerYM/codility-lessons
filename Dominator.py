def solution(A):
    
    num_count = {}
    for num in A:
        num_count[num] = num_count.get(num, 0) + 1
    
    for num, count in num_count.items():
        if count > len(A) // 2:
            return A.index(num)
    
    return -1
	

# https://codility.com/media/train/6-Leader.pdf
	
def solution_2(A):
    
    num_stack = []
    
    for num in A:
        if not num_stack or num_stack[-1] == num:
            num_stack.append(num)
        else:
            num_stack.pop()
        
    if num_stack:
        candidate = num_stack[0]
        count = len([True for num in A if candidate == num])
    
        if count > len(A) // 2:
            return A.index(candidate)
    
    return -1
