# Function to calculate the maximum number of stocks that can be bought
def maxStocks(prices, money):
    # list to store stock price and maximum stocks available on that day
    stockInfo = []
    n = len(prices)
    # Populate the stockInfo list with price and day
    for i in range(n):
        stockInfo.append((prices[i], i + 1))
    # Sort the stockInfo list based on stock prices in ascending order
    stockInfo.sort()
    # Total number of stocks bought
    totalStocksBought = 0
    # Traverse through sorted stock prices
    for i in range(n):
        # Price of the stock
        price = stockInfo[i][0]
        # Max stocks you can buy on this day
        maxStocksOnDay = stockInfo[i][1]
        # Calculate the maximum stocks that can be bought on this day
        stocksToBuy = min(maxStocksOnDay, money // price)
        # Update the total stocks bought and the remaining money
        totalStocksBought += stocksToBuy
        money -= stocksToBuy * price
        # Break if no money is left
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
