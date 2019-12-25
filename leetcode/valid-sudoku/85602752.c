// title: valid-sudoku
// detail: https://leetcode.com/submissions/detail/85602752/
// datetime: Wed Dec 14 11:04:42 2016
// runtime: 3 ms
// memory: N/A

bool checkNumber(char** board, int row, int col, int rowSize, int colSize){
    int c = 0;
    int r = 0;
    int num = board[row][col];
    for(c = 0; c < colSize; c ++){
        if(c != col && board[row][c] == num){
            return false;
        }
    }
    for(r = 0; r < rowSize; r ++){
        if(r != row && board[r][col] == num){
            return false;
        }
    }
    for(r = row -  row % 3; r < row - row % 3 + 3; r ++){
        for(c = col - col % 3; c < col - col % 3 + 3; c ++){
            if(r == row && c == col){
                continue;
            }
            if(board[r][c] == num){
                return false;
            }
        }
    }
    return true;
}
bool isValidSudoku(char** board, int boardRowSize, int boardColSize) {
    int r = 0;
    int c = 0;
    int i = 0;
    for(r = 0; r < boardRowSize; r ++){
        for(c = 0; c < boardColSize; c ++){
            if(board[r][c] == '.') continue;
            if(!checkNumber(board, r, c, boardRowSize, boardColSize)){
                return false;
            }
        }
    }
    return true;
}
