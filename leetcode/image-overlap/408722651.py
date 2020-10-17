# title: image-overlap
# detail: https://leetcode.com/submissions/detail/408722651/
# datetime: Thu Oct 15 02:01:26 2020
# runtime: 1072 ms
# memory: 14 MB

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        def overlap(di, dj):
            o1, o2, o3, o4 = 0, 0, 0, 0
            for i in range(di, n):
                for j in range(dj, n):
                    if img1[i - di][j - dj] == img2[i][j] == 1:
                        o1 += 1
                    if img1[i][j] == img2[i - di][j - dj] == 1:
                        o2 += 1
                    if img1[n - 1 - i + di][j - dj] == img2[-i - 1][j] == 1:
                        o3 += 1
                    if img2[n - 1 - i + di][j - dj] == img1[-i - 1][j] == 1:
                        o4 += 1
            return max(o1, o2, o3, o4)
        
        return max(overlap(di, dj) for di in range(0, n) for dj in range(0, n))
