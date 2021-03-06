def solution(A, B, K):

    front = (A // K) * K if A % K == 0 else (A // K + 1) * K
    rear = (B // K) * K

    # print(front, rear)
    return (rear - front) // K + 1
