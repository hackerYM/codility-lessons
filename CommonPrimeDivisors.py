# https://stackoverflow.com/questions/34251682

def gcd(x, y):

    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

def del_common_primes(x, y):

    while x > 1:
        gcd_xy = gcd(x, y)
        if gcd_xy == 1:
            return x
        x //= gcd_xy

    return x

def solution(A, B):

    count = 0
    for a, b in zip(A, B):
        gcd_ab = gcd(a, b)
        a_remian = del_common_primes(a, gcd_ab)
        b_remian = del_common_primes(b, gcd_ab)
        count += int(a_remian == 1 and b_remian == 1)

    return count
