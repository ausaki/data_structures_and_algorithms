# title: sliding-puzzle
# detail: https://leetcode.com/submissions/detail/412597808/
# datetime: Sat Oct 24 22:24:09 2020
# runtime: 44 ms
# memory: 14.1 MB

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def encode(board):
            state = 0
            for i in range(6):
                state |= board[i // 3][i % 3] << (i * 3)
            return state
        
        def decode(state):
            return [[(state >> ((i * 3 + j) * 3)) & 7 for j in range(3)]  for i in range(2)]
        
        target = encode([[1, 2, 3], [4, 5, 0]])
        start = encode(board)
        q = collections.deque([start])
        visited = {start}
        steps = 0
        while q:
            for _ in range(len(q)):
                st = q.popleft()
                if st == target:
                    return steps
                for p in range(6):
                    if ((st >> (p * 3)) & 7) != 0:
                        continue
                    i, j = divmod(p, 3)
                    for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                        ii, jj = i + di, j + dj
                        if 0 <= ii < 2 and 0 <= jj < 3:
                            k = (ii * 3 + jj)
                            st2 = st
                            st2 |= (((st2 >> (k * 3)) & 7) << (p * 3))
                            st2 &= ~(7 << (k * 3))
                            if st2 == target:
                                return steps + 1
                            if st2 not in visited:
                                visited.add(st2)
                                q.append(st2)
            steps += 1
        return -1
                                    