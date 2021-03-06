def solution(A):

    for idx, num in enumerate(sorted(A)):
        if idx + 1 != num:
            return 0

    return 1


# def solution(A):
#
#     set_A = set(A)
#     return 1 if len(set_A) == len(A) and max(set_A) == len(A) else 0
