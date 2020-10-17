# title: snakes-and-ladders
# detail: https://leetcode.com/submissions/detail/404878832/
# datetime: Tue Oct  6 00:36:21 2020
# runtime: 144 ms
# memory: 14.2 MB

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
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
                    x, y = n2ij(k)
                    jump = board[x][y]
                    if jump != -1:
                        k = jump
                    if not visited[k]:
                        q.append(k)
                        visited[k] = 1
            moves += 1
        return -1