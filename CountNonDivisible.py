# from collections import defaultdict
#
# def factorization(N):
#
#     F = [0] * (N + 1)
#
#     for idx in range(2, int(N ** 0.5) + 1, 1):
#         if F[idx] == 0:
#             for factor in range(idx * idx, N + 1, idx):
#                 if F[factor] == 0:
#                     F[factor] = idx
#
#     return F
#
# def factors(N, F):
#
#     counters = defaultdict(int)
#     while F[N] > 0:
#         counters[F[N]] += 1
#         N //= F[N]
#
#     counters[N] += 1
#     counters[0] = counters[1] = 0
#
#     div = [1]
#     for prime, count in counters.items():
#         div = [d * prime ** e for d in div for e in range(count + 1)]
#
#     return div
#
# def solution(A):
#
#     counters = defaultdict(int)
#     for num in A:
#         counters[num] += 1
#
#     divisors, F = {}, factorization(max(counters.keys()))
#     for num in A:
#         if num not in divisors:
#             divisors[num] = sum(counters[idx] for idx in factors(num, F))
#
#     return [len(A) - divisors[num] for num in A]


def factors(N):

    numbers = set()
    for idx in range(1, int(N ** 0.5) + 1):
        if N % idx == 0:
            numbers.update((idx, N // idx))

    return numbers


def solution(A):

    counters = {}
    for num in A:
        counters[num] = counters.get(num, 0) + 1

    divisors = {}
    for num in A:
        if num not in divisors:
            divisors[num] = sum(counters.get(idx, 0) for idx in factors(num))

    return [len(A) - divisors[num] for num in A]
