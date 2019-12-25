// title: sudoku-solver
// detail: https://leetcode.com/submissions/detail/85531489/
// datetime: Tue Dec 13 15:53:44 2016
// runtime: 16 ms
// memory: N/A

int checkNumber(char** board, char num, int row, int col, int rowSize, int colSize){
    int c = 0;
    int r = 0;
    for(c = 0; c < colSize; c ++){
        if(board[row][c] == num){
            return 0;
        }
    }
    for(r = 0; r < rowSize; r ++){
        if(board[r][col] == num){
            return 0;
        }
    }
    for(r = row -  row % 3; r < row - row % 3 + 3; r ++){
        for(c = col - col % 3; c < col - col % 3 + 3; c ++){
            if(board[r][c] == num){
                return 0;
            }
        }
    }
    return 1;
}

int r_solveSudoku(char** board, int row, int col, int boardRowSize, int boardColSize){
    int r = 0;
    int c = 0;
    int i = 0;
    int findBlank = 0;
    int solved = 0;
    for(r = row; r < boardRowSize && ! findBlank; r ++){
        for(c = (r == row ? col : 0); c < boardColSize && ! findBlank; c ++){
            if(board[r][c] == '.') findBlank = 1;
        }
    }
    if(findBlank){
        r --;
        c --;
    } else {
        return 1;
    }
    for(i = '1'; i <= '9'; i ++){
        if(checkNumber(board, i, r, c, boardRowSize, boardColSize)){
            board[r][c] = i;
            if(c + 1 < boardColSize){
                solved = r_solveSudoku(board, r, c + 1, boardRowSize, boardColSize);
            } else if(r + 1 < boardRowSize){
                solved = r_solveSudoku(board, r + 1, 0, boardRowSize, boardColSize);
            } else {
                solved = 1;
            }
            if(solved){
                break;
            }
            board[r][c] = '.';
        }
    }
    return solved;
}
void solveSudoku(char** board, int boardRowSize, int boardColSize) {
    r_solveSudoku(board, 0, 0, boardRowSize, boardColSize);
}
