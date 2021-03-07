from collections import defaultdict

def solution(A):

    l_counts, r_counts = defaultdict(int), defaultdict(int)
    for num in A:
        r_counts[num] += 1

    leader, equi_count = A[0], 0
    for idx, num in enumerate(A):
        l_counts[num] += 1
        r_counts[num] -= 1

        if l_counts[leader] < l_counts[num]:
            leader = num
        if l_counts[leader] > (idx + 1) // 2 and r_counts[leader] > (len(A) - idx - 1) // 2:
            equi_count += 1

    return equi_count
