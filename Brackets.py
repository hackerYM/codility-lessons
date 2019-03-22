def solution(S):
    
    characters_stack = []
    nested_ch = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    
    for ch in S:
        if ch == "(" or ch == "[" or ch == "{":
            characters_stack.append(ch)
        else:
            if len(characters_stack) == 0:
                return 0
            
            left_ch = characters_stack.pop()
            if nested_ch.get(left_ch) != ch:
                return 0
                
    return 1 if len(characters_stack) == 0 else 0
