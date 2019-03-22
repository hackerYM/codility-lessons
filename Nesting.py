def solution(S):
    
    characters_stack = []

    for ch in S:
        if ch == "(":
            characters_stack.append(ch)
        else:
            if len(characters_stack) == 0:
                return 0
            
            left_ch = characters_stack.pop()
            if ch != ")":
                return 0

    return 1 if len(characters_stack) == 0 else 0
