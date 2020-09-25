# title: minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix
# detail: https://leetcode.com/submissions/detail/393643197/
# datetime: Thu Sep 10 15:12:09 2020
# runtime: 36 ms
# memory: 14 MB

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def flip(bits, k):
            i, j = divmod(k, n)
            bits ^= 1 << k
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
                for k in range(m * n):
                    bits_ = flip(bits, k)
                    if bits_ == 0:
                        return steps + 1
                    if bits_ not in visited:
                        visited.add(bits_)
                        q.append(bits_)
            steps += 1
        return -1