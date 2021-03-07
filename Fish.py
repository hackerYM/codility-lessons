def solution(A, B):

    up_count, down_fishs = 0, []

    for idx in range(len(A)):
        if B[idx] == 1:
            down_fishs.append(A[idx])
        else:
            while down_fishs and down_fishs[-1] < A[idx]:
                down_fishs.pop()

        up_count += int(len(down_fishs) == 0)

    return up_count + len(down_fishs)
