def solution(N, A):
    
    result = [0] * N
    max_num, max_counter = 0, 0

    for num in A:
        if num == N + 1:
            max_counter = max_num
        else:
            result[num-1] = max(result[num-1], max_counter)
            result[num-1] += 1
            max_num = max(max_num, result[num-1])

    for idx in range(N):
        result[idx] = max(result[idx], max_counter)

    return result

