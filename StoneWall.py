def solution(H):
    
    stack = []
    block_count = 0
    
    for height in H:
        while stack and height < stack[-1]:
            stack.pop()
            block_count += 1
        
        if not stack or height > stack[-1]:
            stack.append(height)

        # print(stack, block_count)
        
    return block_count + len(stack)
