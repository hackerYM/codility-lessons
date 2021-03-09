def solution(A, K):

    if len(A) == 0:
        return []

    N = K % len(A)
    return A[-N:] + A[:-N]
