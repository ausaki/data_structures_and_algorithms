// title: minimum-degree-of-a-connected-trio-in-a-graph
// detail: https://leetcode.com/submissions/detail/455806290/
// datetime: Sun Feb 14 12:47:56 2021
// runtime: 1332 ms
// memory: 18.5 MB



int minTrioDegree(int n, int** edges, int edgesSize, int* edgesColSize){
    char m[n][n];
    int deg[n];
    int i, j, k, d, res;
    res = 100000000;
    memset(m, 0, n * n);
    memset(deg, 0, n * sizeof(int));
    for(i = 0; i < edgesSize; i++){
        m[edges[i][0] - 1][edges[i][1] - 1] = 1;
        m[edges[i][1] - 1][edges[i][0] - 1] = 1;
        deg[edges[i][0] - 1] += 1;
        deg[edges[i][1] - 1] += 1;
    }
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            for(k = 0; k < n; k++){
                if(m[i][j] && m[i][k] && m[j][k]){
                    d = deg[i] + deg[j] + deg[k] - 6;
                    if(d < res){
                        res = d;
                    }
                }
            }
        }
    }
    return res != 100000000 ? res : -1;
}