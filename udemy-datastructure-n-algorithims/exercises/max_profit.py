def max_profit(stock_prices):
    """
    Since this is kind of timeseries data,
    to be able to find max profit, the first one we should think
    to find min price to buy

    check if max profit is higher assign max profit
    """
    min_stock_price = stock_prices[0]
    maximun_profit = 0
    for i in range(1, len(stock_prices)):
        if stock_prices[i] < min_stock_price:
            min_stock_price = stock_prices[i]
        elif stock_prices[i] > min_stock_price:
            maximun_profit = max(maximun_profit,
                                 stock_prices[i] - min_stock_price)

    return maximun_profit


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test with mixed prices:
    Prices: [7, 1, 5, 3, 6, 4]
    Maximum profit: 5
    -----------------------------
    Test with descending prices:
    Prices: [7, 6, 4, 3, 1]
    Maximum profit: 0
    -----------------------------
    Test with ascending prices:
    Prices: [1, 2, 3, 4, 5, 6]
    Maximum profit: 5
    -----------------------------

"""
