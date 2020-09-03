# title: parallel-courses-ii
# detail: https://leetcode.com/submissions/detail/380396470/
# datetime: Fri Aug 14 00:13:15 2020
# runtime: 188 ms
# memory: 8.6 MB

class Solution {
public:
    int minNumberOfSemesters(int n, vector<vector<int>>& dependencies, int k) {
        vector<int> pre(n);
        for(auto& e : dependencies){
            e[0] -= 1;
            e[1] -= 1;
            pre[e[1]] |= 1 << e[0];
        }
        vector<int> dp(1 << n, n);
        dp[0] = 0;
        for(int i = 0; i < (1 << n); i += 1){
            int ex = 0;
            for(int j = 0; j < n; j += 1) if((i & pre[j]) == pre[j]) ex |= 1 << j;
            ex &= ~i;
            for(int s = ex; s; s = (s - 1) & ex) if(__builtin_popcount(s) <= k){
                dp[i | s] = min(dp[i | s], dp[i] + 1);
            }
        }
        return dp.back();
    }
};