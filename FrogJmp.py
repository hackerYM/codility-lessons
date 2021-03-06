def solution(X, Y, D):
    
    steps = (Y - X) // D
    return steps if (Y - X) % D == 0 else steps + 1
