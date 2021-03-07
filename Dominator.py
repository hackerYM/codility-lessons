def solution(A):

    num_count = {}
    for num in A:
        num_count[num] = num_count.get(num, 0) + 1

    for num, count in num_count.items():
        if count > len(A) // 2:
            return A.index(num)

    return -1


# https://codility.com/media/train/6-Leader.pdf

def solution_2(A):

    size, value = 0, None
    for num in A:
        if size == 0:
            size, value = 1, num
        elif num == value:
            size += 1
        else:
            size -= 1

    if value == None:
        return -1

    count = sum(1 if num == value else 0 for num in A)
    return A.index(value) if count > len(A) // 2 else -1
