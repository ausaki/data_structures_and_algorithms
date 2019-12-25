// title: best-time-to-buy-and-sell-stock
// detail: https://leetcode.com/submissions/detail/190687367/
// datetime: Tue Nov 20 16:54:05 2018
// runtime: 0 ms
// memory: N/A

int maxProfit(int* prices, int pricesSize) {
    if(pricesSize == 0){
        return 0;
    }
    int i = 0;
    int min_price = prices[0];
    int max_profit = 0;
    int d = 0;
    for(i = 0; i < pricesSize; i++){
        d = prices[i] - min_price;
        if(d < 0){
            min_price = prices[i];
        } else if(d > max_profit){
            max_profit = d;
        }
    }
    return max_profit;
}