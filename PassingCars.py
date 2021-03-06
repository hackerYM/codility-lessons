def solution(A):

    easts, passings = 0, 0

    for travel in A:
        if travel == 0:
            easts += 1
        else:
            passings += easts

    return -1 if passings > 1_000_000_000 else passings
