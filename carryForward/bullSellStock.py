# Best Time to Buy and Sell Stock I (Single Transaction)
# Problem Understanding
# This problem asks us to find the maximum profit we can achieve by buying and 
# selling a stock with at most one transaction. We must buy before selling, and 
# we want to maximize the profit (sell price - buy price).


def bestTimetoBuySell(A):

    min_price=float('inf')
    max_profit=0

    for price in A:
        min_price=min(min_price,price)

        profit=price-min_price

        max_profit=max(max_profit,profit)

    return max_profit

A=[1, 4, 5, 2, 4]
print(f"max profit : {bestTimetoBuySell(A)}")         
