# title: minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix
# detail: https://leetcode.com/submissions/detail/393642459/
# datetime: Thu Sep 10 15:10:08 2020
# runtime: 44 ms
# memory: 13.8 MB

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def flip(bits, i, j):
            bits ^= 1 << (i * n + j)
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n:
                    bits ^= 1 << (ii * n + jj)
            return bits
        
        m, n = len(mat), len(mat[0])
        bits = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    k = i * n + j
                    bits |= 1 << k
        q = collections.deque([bits])
        visited = {bits}
        steps = 0
        while q:
            for _ in range(len(q)):
                bits = q.popleft()
                if bits == 0:
                    return steps
                for i in range(m):
                    for j in range(n):
                        bits_ = flip(bits, i, j)
                        if bits_ == 0:
                            return steps + 1
                        if bits_ not in visited:
                            visited.add(bits_)
                            q.append(bits_)
            steps += 1
        return -1