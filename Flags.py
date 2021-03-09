def solution(A):

    peaks = [idx for idx in range(1, len(A)-1) if A[idx-1] < A[idx] > A[idx+1]]
    if len(peaks) < 3:
        return len(peaks)

    nexts = []
    for peak in peaks:
        nexts += [peak] * (peak - len(nexts) + 1)

    max_flag = [i for i in range(len(A)) if i * (i-1) <= peaks[-1] - peaks[0]][-1]
    for flag in range(max_flag, 2, -1):
        distances, cur_peak = 0, peaks[0]
        while cur_peak < peaks[-1] and cur_peak + flag < len(nexts):
            distances += 1
            cur_peak = nexts[cur_peak + flag]

        if distances + 1 >= flag:
            return flag

    return 2
