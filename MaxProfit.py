import sys

def solution(A):
    
    min_share = sys.maxsize
    max_profit = 0
    
    for share in A:
        if share < min_share:
            min_share = share
        
        if share - min_share > max_profit:
            max_profit = share - min_share
            
    return max_profit
