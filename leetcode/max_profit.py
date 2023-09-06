"""
Best Time to Buy and Sell Stock.

You are given an array prices where prices[i] is the price of a given stock

on the ith day. You want to maximize your profit by choosing a single day to

buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.

If you cannot achieve any profit, return 0.
"""
from typing import List

test_prices = [7, 1, 5, 3, 6, 4]


def max_profit_func(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


print(max_profit_func(test_prices))
