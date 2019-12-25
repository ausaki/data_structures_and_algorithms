# title: battleships-in-a-board
# detail: https://leetcode.com/submissions/detail/285690753/
# datetime: Fri Dec 13 20:47:10 2019
# runtime: 72 ms
# memory: 13.4 MB

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        '''
        O O O O O O O O O O
        O X X X O X O X X O 
        O O O O O X O O O O 
        O X O X O X O X X O 
        O X O X O X O O O O 
        O O O O O O O O O O 
        (在最外围加上一层 O)
        
        可以看出战列舰其实被一圈O围起来了, 因此只要统计矩形的数量就行了.
        '''
        M = len(board)
        if M == 0: return 0
        N = len(board[0])
        res = 0
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                    res += 1
        return res
        
                