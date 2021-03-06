def solution(N):

    # print("{0:b}".format(N))
    result, gap, first = 0, 0, False

    while N > 0:
        bit = N % 2
        N = N // 2

        if bit == 1:
            if first:
                result = max(result, gap)
            gap, first = 0, True
        else:
            gap = gap + 1

    return result
