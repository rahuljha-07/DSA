int maxProfit (vector<int> a) {
    int Profit = 0;
    for (int i=1; i <a.length; i++) {
            if (a[i]> a[i-1]) Profit += (a[i]-a[i-1]);
    }
return Profit;
}
// selling and buying on the same day with any tranction to get max