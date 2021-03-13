def solution(N, M):

    n, gcd = N, M
    while n % gcd != 0:
        n, gcd = gcd, n % gcd

    lcm = (N * M) // gcd
    return lcm // M
