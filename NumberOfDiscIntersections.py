# Brute Force O(N ** 2)

# def solution(A):
#
#     result = 0
#
#     for r_idx in range(len(A)):
#         for l_idx in range(r_idx + 1, len(A)):
#             if r_idx + A[r_idx] >= l_idx - A[l_idx]:
#                 result += 1
#
#     return -1 if result > 10_000_000 else result

# http://www.lucainvernizzi.net/blog/2014/11/21/codility-beta-challenge-number-of-disc-intersections/

def solution(A):

    boundaries = []
    for idx, radius in enumerate(A):
        boundaries += [(idx-radius, +1), (idx+radius, -1)]

    boundaries.sort(key=lambda x: (x[0], -x[1]))
    intersects, overlapped_circles = 0, 0

    for _, count_delta in boundaries:
        intersects += overlapped_circles * int(count_delta > 0)
        overlapped_circles += count_delta

    # print(boundaries)
    return -1 if intersects > 10_000_000 else intersects
