def solution(N):

    idx, factors = 1, 0

    while idx * idx < N:
        if N % idx == 0:
            factors += 2
        idx += 1

    if idx * idx == N:
        factors += 1

    return factors
