def solution(A):  # Complexity: Time O(N**2)

    A.sort()
    count = 0

    for x in range(0, len(A)):
        z = x + 2
        for y in range(x + 1, len(A)):
            while z < len(A) and A[x] + A[y] > A[z]:
                z += 1
            count += z - y - 1

    return count
