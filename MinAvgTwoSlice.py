# https://github.com/daotranminh/playground/blob/master/src/codibility/MinAvgTwoSlice/proof.pdf

def solution(A):

    if len(A) <= 2:
        return 0

    min_idx, min_val = 0, 10_001
    for idx in range(0, len(A) - 2):
        if (A[idx] + A[idx+1]) / 2 < min_val:
            min_idx, min_val = idx, (A[idx] + A[idx+1]) / 2
        if (A[idx] + A[idx+1] + A[idx+2]) / 3 < min_val:
            min_idx, min_val = idx, (A[idx] + A[idx+1] + A[idx+2]) / 3

    idx = len(A) - 2
    if (A[idx] + A[idx+1]) / 2 < min_val:
        min_idx, min_val = idx, (A[idx] + A[idx+1]) / 2

    return min_idx
