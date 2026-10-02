def maxStocks(prices, money):
    stockInfo = []
    n = len(prices)
    for i in range(n):
        stockInfo.append((prices[i], i + 1))
    stockInfo.sort()
    totalStocksBought = 0
    for i in range(n):
        price = stockInfo[i][0]
        maxStocksOnDay = stockInfo[i][1]
        stocksToBuy = min(maxStocksOnDay, money // price)
        totalStocksBought += stocksToBuy
        money -= stocksToBuy * price
        if money <= 0:
            break
    return totalStocksBought


def main():
    prices = [10, 7, 19]
    money = 45
    result = maxStocks(prices, money)
    print("Maximum stocks bought:", result)


if __name__ == "__main__":
    main()


'''
Let n be trading days.
Time: O(n log(n+1)): build/sort price-day pairs and scan them once.
The purchase amount is computed directly, not one iteration per stock.
Space: O(n) auxiliary stockInfo/sorting workspace; prices is unchanged.
Prices must be positive and money nonnegative; day i permits i+1 stocks.
'''
