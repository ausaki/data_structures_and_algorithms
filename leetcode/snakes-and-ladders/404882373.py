# title: snakes-and-ladders
# detail: https://leetcode.com/submissions/detail/404882373/
# datetime: Tue Oct  6 00:46:08 2020
# runtime: 124 ms
# memory: 14.1 MB

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def ij2n(i, j):
            k = (n - i - 1) * n
            if (n - i - 1) % 2:
                return k + j + 1
            return k + n - j
        
        def n2ij(x):
            i, j = divmod((x - 1), n)
            if i % 2 == 0:
                return n - i - 1, j
            return n - i - 1, n - j - 1
        q = collections.deque([1])
        moves = 0
        visited = [0] * (n * n + 1)
        visited[1] = 1
        while q:
            # print(q)
            for i in range(len(q)):
                j = q.popleft()
                if j == n * n:
                    return moves
                for k in range(j + 1, min(j + 7, n * n + 1)):
                    if k == n * n:
                        return moves + 1
                    x, y = n2ij(k)
                    jump = board[x][y]
                    if jump == n * n:
                        return moves + 1
                    if jump != -1:
                        k = jump
                    if not visited[k]:
                        q.append(k)
                        visited[k] = 1
            moves += 1
        return -1