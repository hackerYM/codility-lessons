# def solution(A):  # Complexity: Time O(N), Space O(N)
#
#     return len(set(abs(num) for num in A))

def solution(A):  # Complexity: Time O(N), Space O(1)

    count = 0
    front, rear = 0, len(A) - 1

    while front <= rear:
        while front != rear and A[front] == A[front+1]:  # adjusted duplicate numbers
            front += 1
        while front != rear and A[rear] == A[rear-1]:
            rear -= 1

        if abs(A[front]) - abs(A[rear]) == 0:  # absolute duplicate numbers
            front += 1
            rear -= 1
        elif abs(A[front]) > abs(A[rear]):
            front += 1
        else:
            rear -= 1

        count += 1

    return count
