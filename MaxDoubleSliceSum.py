# use Kadane’s algorithm from two directions
# https://rafal.io/posts/codility-max-double-slice-sum.html


def solution(A):
    
    N = len(A)
    inc_sum, dec_sum = [0] * N, [0] * N
    
    for idx in range(1, N-1):
        inc_sum[idx] = max(0, inc_sum[idx-1] + A[idx])
    
    for idx in reversed(range(1, N-1)):
        dec_sum[idx] = max(0, dec_sum[idx+1] + A[idx])
    
    # print("\n{}\n{}\n".format(inc_sum, dec_sum))
    
    max_double_slice_sum = 0
    for idx in range(1, N-1):
        max_double_slice_sum = max(max_double_slice_sum, inc_sum[idx-1] + dec_sum[idx+1])
    
    return max_double_slice_sum
