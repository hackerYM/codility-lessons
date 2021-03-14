def solution(A, B):

    count = len(A)
    overlap_idx = 0

    for idx in range(1, len(A)):
        if A[idx] <= B[overlap_idx]:
            count -= 1
        else:
            overlap_idx = idx

    return count

#    ==     --> o
#   ==      --> x
#  ==       --> x
# ==    ==  --> o
