# http://www.lucainvernizzi.net/blog/2014/11/21/codility-beta-challenge-number-of-disc-intersections/

def solution(A):
    
    circle_boundary = []
    for idx, radius in enumerate(A):
        circle_boundary += [(idx-radius, +1), (idx+radius, -1)]
        
    circle_boundary.sort(key=lambda x: (x[0], -x[1]))
    # print(circle_boundary)
    
    intersection, overlapped_circle = 0, 0
    for _, boundary_delta in circle_boundary:
        intersection += overlapped_circle * int(boundary_delta > 0)
        overlapped_circle += boundary_delta
        
        if intersection > 10E6:
            return -1
    
    return intersection
