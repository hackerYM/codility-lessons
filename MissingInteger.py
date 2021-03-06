def solution(A):
    
    counts = [0] * (max(A) + 1)

    for num in A:
        if num > 0:
            counts[num - 1] += 1

    for idx, count in enumerate(counts):
        if count == 0:
            return idx + 1

    return 1

