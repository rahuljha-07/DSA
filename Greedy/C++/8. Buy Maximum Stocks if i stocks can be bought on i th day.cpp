#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to calculate the maximum number of stocks that can be bought
int maxStocks(vector<int>& prices, int money) {
    // Vector to store stock price and maximum stocks available on that day
    vector<pair<int, int>> stockInfo;
    int n = prices.size();

    // Populate the stockInfo vector with price and day
    for (int i = 0; i < n; ++i) {
        stockInfo.push_back({prices[i], i + 1});
    }

    // Sort the stockInfo vector based on stock prices in ascending order
    sort(stockInfo.begin(), stockInfo.end());

    int totalStocksBought = 0; // Total number of stocks bought

    // Traverse through sorted stock prices
    for (int i = 0; i < n; ++i) {
        int price = stockInfo[i].first;  // Price of the stock
        int maxStocksOnDay = stockInfo[i].second;  // Max stocks you can buy on this day

        // Calculate the maximum stocks that can be bought on this day
        int stocksToBuy = min(maxStocksOnDay, money / price);

        // Update the total stocks bought and the remaining money
        totalStocksBought += stocksToBuy;
        money -= stocksToBuy * price;

        // Break if no money is left
        if (money <= 0) break;
    }

    return totalStocksBought;
}

int main() {
    vector<int> prices = {10, 7, 19};  // Prices of stocks for each day
    int money = 45;  // Initial amount of money available

    // Function call to calculate maximum stocks
    int result = maxStocks(prices, money);

    // Print the result
    cout << "Maximum stocks bought: " << result << endl;

    return 0;
}
