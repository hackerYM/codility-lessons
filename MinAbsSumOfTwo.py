def solution(A):  # Complexity: Time O(N*log(N))

    min_val = 2_000_000_000
    front, rear = 0, len(A) - 1

    A.sort()
    while front <= rear:
        min_val = min(min_val, abs(A[front] + A[rear]))
        if abs(A[front]) > abs(A[rear]):
            front += 1
        else:
            rear -= 1

    return min_val
