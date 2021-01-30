# title: find-minimum-time-to-finish-all-jobs
# detail: https://leetcode.com/submissions/detail/441061707/
# datetime: Sun Jan 10 16:02:56 2021
# runtime: 1300 ms
# memory: 13.8 MB

class Solution {
public:
    bool check(int mid, vector<int>& a, int k, vector<int>& subsum) {
        int n = a.size();
        vector<int> dp(1 << n, 1e9);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int rem = ((1 << n) - 1) ^ mask;
            for (int sub = rem; sub; sub = (sub - 1) & rem)
                if (subsum[sub] <= mid)
                    dp[mask ^ sub] = min(dp[mask ^ sub], dp[mask] + 1);
        }
        return dp[(1 << n) - 1] <= k;
    }
    
    int minimumTimeRequired(vector<int>& a, int k) {
        int n = a.size();
        
        vector<int> sub(1 << n);
        for (int i = 0; i < (1 << n); i++) {
            for (int j = 0; j < n; j++) {
                if(i & (1 << j)) {
                    sub[i] += a[j];
                }
            }
        }
        
        int mx = -1, sum = 0;
        for(int x : a) {
            mx = max(mx, x);
            sum += x;
        }
        int l = mx, r = sum;
        
        
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if(check(mid, a, k, sub)) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};

