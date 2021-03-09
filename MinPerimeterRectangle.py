from math import floor, sqrt

def solution(N):

    idx = floor(sqrt(N))

    for edge in reversed(range(2, idx+1)):
        if N % edge == 0:
            return (edge + (N // edge)) * 2

    return (1 + N) * 2
