import sys


def solution(A):

    front, rear = 0, sum(A)
    result = sys.maxsize

    for num in A[:-1]:
        front += num
        rear -= num
        result = min(result, abs(front - rear))

    return result
