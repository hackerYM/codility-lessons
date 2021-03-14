# def solution(M, A):  # Complexity: Time O(N**3)
#
#     count = 0
#
#     for i in range(0, len(A)):
#         for j in range(i, len(A)):
#             if len(A[i:j+1]) == len(set(A[i:j+1])):
#                 count += 1
#
#     return count

# [3, 4, 5, 5, 2, 2] --> 1 + 2 + 3 + 1 + 2 + 1
# [3, 4, 5, 4, 5, 6] --> 1 + 2 + 3 + 2 + 2 + 3

def solution(M, A):  # Complexity: Time O(N)

    count, nums_count = 0, [0] * (M + 1)
    back = front = 0

    for num in A:
        if nums_count[num] > 0:
            for idx in range(back, front, 1):
                if A[back] == num:
                    nums_count[A[back]] -= 1
                    back += 1
                    break
                else:
                    nums_count[A[back]] -= 1
                    back += 1

        front += 1
        nums_count[num] += 1
        count += front - back

    return min(1_000_000_000, count)
