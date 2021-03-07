def solution(H):

    blocks, stack = 0, []

    for height in H:
        while stack and stack[-1] > height:
            stack.pop()
            blocks += 1

        if not stack or stack[-1] < height:
            stack.append(height)

    return blocks + len(stack)
