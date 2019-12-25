// title: unique-paths-ii
// detail: https://leetcode.com/submissions/detail/145528559/
// datetime: Sat Mar 17 15:00:44 2018
// runtime: 0 ms
// memory: N/A

int uniquePaths_(int** obstacleGrid, int row, int col, int m, int n, int** cache){
    if(cache[m][n] != -1){
        return cache[m][n];
    }
    int p = 0;
    if(n + 1 < col && obstacleGrid[m][n + 1] == 0){
        p += uniquePaths_(obstacleGrid, row, col, m, n + 1, cache);
    }
    if(m + 1 < row && obstacleGrid[m + 1][n] == 0){
        p += uniquePaths_(obstacleGrid, row, col, m + 1, n, cache);
    }
    cache[m][n] = p;
    return cache[m][n];
}

int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridRowSize, int obstacleGridColSize) {
    int m = obstacleGridRowSize;
    int n = obstacleGridColSize;
    int** cache = (int**)malloc(m * sizeof(int*));
    
    int i, j;
    for(i = 0; i < m; i ++){
        cache[i] = (int*)malloc(n * sizeof(int));
        for(j = 0; j < n; j++){
            if(obstacleGrid[i][j] == 1){
                cache[i][j] = 0;
            } else{
                if(i == m - 1 && j == n - 1){
                    cache[i][j] = 1;
                } else{
                    cache[i][j] = -1;
                }
            }
        }
    }
    return uniquePaths_(obstacleGrid, m, n, 0, 0, cache);
}