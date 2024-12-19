int maxProfit(vector<int>& prices) {
    int n = prices.size();
    int sellPrice = prices[n - 1];
    int profit = 0;

    // Iterate from the second last element to the beginning
    for (int i = n - 2; i >= 0; i--) {
        // Update the maximum sell price if current price is higher
        if (prices[i] > sellPrice) {
            sellPrice = prices[i];
        }

        // Calculate potential profit and update if it's the maximum
        profit = max(profit, sellPrice - prices[i]);
    }

    return profit;
}
