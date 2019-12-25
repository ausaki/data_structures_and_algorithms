# title: best-time-to-buy-and-sell-stock-iv
# detail: https://leetcode.com/submissions/detail/275273586/
# datetime: Sat Nov  2 16:55:22 2019
# runtime: 8 ms
# memory: 9.1 MB

class Solution {
public:
   int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        if(k == 0 || n == 0)    return 0;
        if(k >= n/2)    return maxProfit(prices);
        vector<int>curr(n,0), prev(n, 0);
        
        for(int i = 1; i <= k; i++){
            int maxDiff = -prices[0];
            for(int j = 1; j < n; j++){
                curr[j] = max(curr[j-1], prices[j] + maxDiff);
                maxDiff = max(maxDiff, prev[j] - prices[j]);
            }
            prev = curr;
        }
        return curr[n-1];
    }
    int maxProfit(vector<int>prices){
        int profit = 0;
        for(int i = 1; i < prices.size(); i++)
            profit += prices[i] > prices[i-1] ? prices[i] - prices[i-1] : 0;
        return profit;
    }
};