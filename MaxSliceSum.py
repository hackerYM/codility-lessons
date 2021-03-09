# Kadane’s algorithm

def solution(A):

    max_ending = max_slice = A[0]

    for number in A[1:]:
        max_ending = max(number, max_ending + number)
        max_slice = max(max_slice, max_ending)

    return max_slice
