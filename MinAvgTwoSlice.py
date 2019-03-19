# https://github.com/daotranminh/playground/blob/master/src/codibility/MinAvgTwoSlice/proof.pdf

import sys

def solution(A):
    
    min_value = sys.maxsize
    min_idx = 0
    
    for i in range(0, len(A)-1):
        
        two_slice_avg = (A[i] + A[i+1]) / 2
        if two_slice_avg < min_value:
            min_value = two_slice_avg
            min_idx = i
        
        if i < len(A)-2:
            three_slice_avg = (A[i] + A[i+1] + A[i+2]) / 3
            if three_slice_avg < min_value:
                min_value = three_slice_avg
                min_idx = i

    return min_idx
