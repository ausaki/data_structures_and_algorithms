// title: best-time-to-buy-and-sell-stock-ii
// detail: https://leetcode.com/submissions/detail/190863066/
// datetime: Wed Nov 21 14:57:09 2018
// runtime: 0 ms
// memory: N/A

int maxProfit(int* prices, int pricesSize) {
    int max_profit = 0;
    int i = 0;
    for(i = 0; i < pricesSize - 1; i++){
        if(prices[i] < prices[i + 1]){
            max_profit += (prices[i + 1] - prices[i]);
        }
    }
    return max_profit;
}