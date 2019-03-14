def solution(N):
    
    bit_count, bit_idx_array = 1, []
    
    while N > 0:
        if N % 2 == 1:
            bit_idx_array.append(bit_count)
        bit_count += 1
        N //= 2
    
    if len(bit_idx_array) < 2:
        return 0
    
    max_gap = 0
    for idx in range(1, len(bit_idx_array)):
        bit_gap = bit_idx_array[idx] - bit_idx_array[idx-1] - 1
        if bit_gap > max_gap:
            max_gap = bit_gap
    
    return max_gap
