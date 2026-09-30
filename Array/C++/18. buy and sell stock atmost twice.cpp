int maxProfit(vector<int> price, int n){
    vector<int>(n, 0) profit; 
    int max_price = price[n-1];
    // selling and buying , doing 2nd tranc from back
    for (int i = n - 2; i >= 0; i--) {
        if (price[i] > max_price) max_price = price[i];
        profit[i] = max(profit[i + 1], max_price - price[i]);
    }
    int min_price = price[0];
    // buying and selling, doing 1st tranction from front and also updating arrayS
    for (int i = 1; i < n; i++) {
        if (price[i] < min_price) min_price = price[i];
        profit[i] = max(profit[i - 1], profit[i] + (price[i] - min_price));
    }
    return profit[n-1];
}    