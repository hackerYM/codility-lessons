def solution(A):

    peaks = [idx for idx in range(1, len(A)-1) if A[idx-1] < A[idx] > A[idx+1]]
    if len(peaks) < 2:
        return len(peaks)

    nexts = []
    for peak in peaks:
        nexts += [peak] * (peak - len(nexts) + 1)
        nexts[peak] = -peak

    nexts += [0] * (len(A) - len(nexts))
    for size in range(len(peaks), 0, -1):
        if len(A) % size == 0:
            block_size = (len(A) // size)
            firsts = (idx * block_size for idx in range(size))
            lasts = ((idx+1) * block_size - 1 for idx in range(size))

            if all(nexts[first] != nexts[last] for first, last in zip(firsts, lasts)):
                return size

    return 0
