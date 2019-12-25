// title: unique-paths
// detail: https://leetcode.com/submissions/detail/145525226/
// datetime: Sat Mar 17 14:29:39 2018
// runtime: 0 ms
// memory: N/A

int uniquePaths_(int m, int n, int** cache){
    if(cache[m - 1][n - 1] > 0){
        return cache[m - 1][n - 1];
    }
    cache[m - 1][n - 1] = uniquePaths_(m, n - 1, cache) + uniquePaths_(m - 1, n, cache);
    return cache[m - 1][n - 1];
}

int uniquePaths(int m, int n) {
    int** cache = (int**)malloc(m * sizeof(int*));
    
    int i, j;
    for(i = 0; i < m; i ++){
        cache[i] = (int*)malloc(n * sizeof(int));
        for(j = 0; j < n; j++){
            if(i == 0 || j == 0){
                cache[i][j] = 1;
            } else{
                cache[i][j] = 0;
            }
        }
    }
    return uniquePaths_(m, n, cache);
}