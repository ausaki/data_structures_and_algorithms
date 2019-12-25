# title: word-search
# detail: https://leetcode.com/submissions/detail/252962277/
# datetime: Mon Aug 19 17:55:08 2019
# runtime: 268 ms
# memory: 14.9 MB

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 广度搜索 + 回溯
        rows = len(board)
        cols = len(board[0])
        i = 0
        j = 0
        track = [[0] * cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    track[i][j] = 1
                    exists = self.backtrack_search(board, word, track, i, j, 1)
                    track[i][j] = 0
                    if exists:
                        return True
        return False

    def backtrack_search(self, board, word, track, row, col, k):
        if k == len(word):
            return True
        rows = len(board)
        cols = len(board[0])
        for i, j in [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]:
            if 0 <= i < rows and 0 <= j < cols and track[i][j] == 0 and board[i][j] == word[k]:
                track[i][j] = 1
                exists = self.backtrack_search(board, word, track, i, j, k + 1)
                track[i][j] = 0
                if exists:
                    return True
        return False
