# def semiprimes(N):
#
#     numbers = [True] * (N + 1)
#     numbers[0] = numbers[1] = False
#
#     for idx in range(2, int(N ** 0.5) + 1, 1):
#         if numbers[idx]:
#             for factor in range(idx * idx, N + 1, idx):
#                 numbers[factor] = False
#
#     primes = [idx for idx in range(N + 1) if numbers[idx]]
#     semiprimes = []
#
#     for i in range(0, len(primes)):
#         for j in range(i, len(primes)):
#             if primes[i] * primes[j] > N:
#                 break
#             semiprimes.append(primes[i] * primes[j])
#
#     return sorted(semiprimes)
#
# def solution(N, P, Q):
#
#     counts = [0]
#     for idx, semiprime in enumerate(semiprimes(N)):
#         counts += [idx] * (semiprime - len(counts) + 1)
#
#     counts += [counts[-1] + 1] * (N - len(counts) + 2)
#     return [counts[q+1] - counts[p] for p, q in zip(P, Q)]

def factorization(N):

    F = [0] * (N + 1)

    for idx in range(2, int(N ** 0.5) + 1, 1):
        if F[idx] == 0:
            for factor in range(idx * idx, N + 1, idx):
                if F[factor] == 0:
                    F[factor] = idx

    return F

def solution(N, P, Q):

    F = factorization(N)

    count, semiprimes = 0, [0] * 4
    for number in range(4, N + 1, 1):
        if F[number] != 0 and F[number // F[number]] == 0:
            count += 1
        semiprimes.append(count)

    return [semiprimes[q] - semiprimes[p-1] for p, q in zip(P, Q)]
