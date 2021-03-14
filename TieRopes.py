def solution(K, A):

    count, length = 0, 0

    for rope in A:
        length += rope
        if length >= K:
            count, length = count + 1, 0

    return count
