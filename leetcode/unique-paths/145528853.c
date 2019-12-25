// title: unique-paths
// detail: https://leetcode.com/submissions/detail/145528853/
// datetime: Sat Mar 17 15:03:41 2018
// runtime: 0 ms
// memory: N/A

int uniquePaths_(int m, int n, int** cache){
    if(cache[m][n] != -1){
        return cache[m][n];
    }
    cache[m][n] = uniquePaths_(m, n + 1, cache) + uniquePaths_(m + 1, n, cache);
    return cache[m][n];
}

int uniquePaths(int m, int n) {
    int** cache = (int**)malloc(m * sizeof(int*));
    
    int i, j;
    for(i = 0; i < m; i ++){
        cache[i] = (int*)malloc(n * sizeof(int));
        for(j = 0; j < n; j++){
            if(i == m - 1 || j == n - 1){
                cache[i][j] = 1;
            } else{
                cache[i][j] = -1;
            }
        }
    }
    return uniquePaths_(0, 0, cache);
}