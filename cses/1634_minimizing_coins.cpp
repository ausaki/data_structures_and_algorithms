#include <bits/stdc++.h>
using namespace std;

typedef unordered_map<int, unordered_map<int, int>> Cache;
typedef unordered_map<int, int> Ints;

int solution(int target, vector<int>* values, int k, Cache* cache) {
  Cache::iterator cit;
  // cout << target << " -- " << k << endl;
  // for(cit = cache->begin(); cit != cache->end(); ++cit){
  //   cout << cit->first << " " << cit->second.size() << endl;
  // }
  if(target == 0){
    return 0;
  }
  // if((cit = cache->find(target)) != cache->end()){
  //   Ints::iterator it;
  //   if((it = cit->second.find(k)) != cit->second.end()){
  //     return it->second;
  //   }
  // }
  int res = 1e9;
  int value = (*values)[k];
  int q = target / value;
  int r = target % value;
  int s = 0;

  if(r == 0){
    res = q;
  } else if(k != 0){
    for(;q >= 0; --q){
      s = solution(r, values, k - 1, cache);
      res = res < q + s ? res : q + s;
      r += value;
    }
  }
  // if((cit = cache->find(target)) == cache->end()){
  //   unordered_map<int, int> mm;
  //   mm[k] = res;
  //   (*cache)[target] = mm;
  // }else{
  //   cit->second[k] = res;
  // }
  return res;
}

int main() {
  int n, target;
  cin >> n >> target;
  vector<int> c(n);
  vector<int> values;
  for (int&v : c) cin >> v;

  // vector<int> dp(target+1,1e9);
  // dp[0] = 0;
  // for (int i = 1; i <= target; i++) {
  //   for (int j = 0; j < n; j++) {
  //     if (i-c[j] >= 0) {
	// dp[i] = min(dp[i], dp[i-c[j]]+1);
  //     }
  //   }
  // }
  // cout << (dp[target] == 1e9 ? -1 : dp[target]) << endl;
  Cache cache;
  sort(c.begin(), c.end());
  vector<int>::iterator it = unique(c.begin(), c.begin() + c.size());
  for(it = c.begin(); it != c.end(); ++it){
    values.push_back(*it);
  }
  int res = solution(target, &values, values.size() - 1, &cache);
  cout << res << endl;
}

