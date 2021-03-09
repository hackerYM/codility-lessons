def solution(A):

    result = 0
    for num in A:
        result ^= num

    return result
