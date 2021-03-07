def solution(S):

    stack = []
    nested_ch = {"(": ")", "[": "]", "{": "}"}

    for ch in S:
        if ch in nested_ch.keys():
            stack.append(ch)
        elif len(stack) == 0 or nested_ch[stack.pop()] != ch:
            return 0

    return int(len(stack) == 0)
