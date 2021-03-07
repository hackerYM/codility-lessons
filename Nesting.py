def solution(S):

    stack = []

    for ch in S:
        if ch == "(":
            stack.append(ch)
        elif len(stack) == 0 or stack.pop() != "(":
            return 0

    return int(len(stack) == 0)
