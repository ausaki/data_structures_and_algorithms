#include <iostream>
#include <stack>
#include <string>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

struct dsu_save {
    int v, rnkv, u, rnku;

    dsu_save() {}

    dsu_save(int _v, int _rnkv, int _u, int _rnku)
        : v(_v), rnkv(_rnkv), u(_u), rnku(_rnku) {}
};

struct dsu_with_rollbacks {
    vector<int> p;
    int comps;
    stack<dsu_save> op;

    dsu_with_rollbacks() {}

    dsu_with_rollbacks(int n) {
        p.resize(n);
        for (int i = 0; i < n; i++) {
            p[i] = -1;
        }
        comps = n;
    }

    int find_set(int v) {
        return (p[v] < 0) ? v : find_set(p[v]);
    }

    bool unite(int v, int u) {
        v = find_set(v);
        u = find_set(u);
        if (v == u)
            return false;
        comps--;
        op.push(dsu_save(v, p[v], u, p[u]));
        if(p[v] < p[u]){
            p[u] = v;
        } else{
            if(p[v] == p[u]){
                p[u] -= 1;
            }
            p[v] = u;
        }
        return true;
    }

    void rollback(int n) {
        for(;n > 0 && !op.empty(); n--){
            dsu_save x = op.top();
            op.pop();
            comps++;
            p[x.v] = x.rnkv;
            p[x.u] = x.rnku;
        }
    }
};

struct query {
    int v, u;
    query(int _v, int _u) : v(_v), u(_u) {
    }
};

struct QueryTree {
    vector<vector<query>> t;
    dsu_with_rollbacks dsu;
    int T;
    vector<bool> ans;

    QueryTree() {}

    QueryTree(int n, int _T) : T(_T) {
        dsu = dsu_with_rollbacks(n);
        t.resize(4 * T);
    }

    void add_to_tree(int v, int l, int r, int ul, int ur, query& q) {
        if (ul > ur)
            return;
        if (l == ul && r == ur) {
            t[v].push_back(q);
            return;
        }
        int mid = (l + r) / 2;
        add_to_tree(2 * v + 1, l, mid, ul, min(ur, mid), q);
        add_to_tree(2 * v + 2, mid + 1, r, max(ul, mid + 1), ur, q);
    }

    void add_query(query q, int l, int r) {
        add_to_tree(0, 0, T - 1, l, r, q);
    }

    void dfs(int v, int l, int r, vector<pair<int, int>>& q) {
        int ops = 0;
        for (query& q : t[v]) {
            ops += dsu.unite(q.v, q.u);
        }
        if (l == r){
            if(q[l].first >= 0){
                ans.push_back(dsu.find_set(q[l].first) == dsu.find_set(q[l].second));
            }
        }
        else {
            int mid = (l + r) / 2;
            dfs(2 * v + 1, l, mid, q);
            dfs(2 * v + 2, mid + 1, r, q);
        }
        dsu.rollback(ops);
    }

    vector<bool> solve(vector<pair<int, int>> q) {
        dfs(0, 0, T - 1, q);
        return ans;
    }
};

int main(){
    int n, m, u, v;
    int op;
    map<pair<int, int>, int> mp;
    // freopen("connect.in", "r", stdin);
    // freopen("connect.out", "w", stdout);
    scanf("%d %d", &n, &m);
    if(m == 0){
        return 0;
    }
    QueryTree qt(n, m);
    vector<pair<int, int>> q(m);
    for(int i = 0; i < m; i++){
        scanf("%d %d %d", &op, &u, &v);
        u -= 1;
        v -= 1;
        if(u > v) swap(u, v);
        pair<int, int> edge = make_pair(u, v);
        q[i] = make_pair(-1, -1);
        if(op == 0){
            mp[edge] = i;
        } else if(op == 1){
            qt.add_query(query(u, v), mp[edge], i - 1);
            mp.erase(edge);
        } else{
            q[i] = edge;
        }
    }
    for(auto it : mp){
        qt.add_query(query(it.first.first, it.first.second), it.second, m - 1);
    }
    vector<bool> ans = qt.solve(q);
    for(auto i: ans){
        printf(i ? "Y\n" : "N\n");
    }
    return 0;
}