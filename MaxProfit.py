def solution(A):

    min_price, max_profit = 200_001, 0

    for price in A:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
