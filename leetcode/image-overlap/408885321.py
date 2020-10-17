# title: image-overlap
# detail: https://leetcode.com/submissions/detail/408885321/
# datetime: Thu Oct 15 11:13:42 2020
# runtime: 480 ms
# memory: 14.5 MB

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        overlaps = collections.Counter()
        pos1 = ((i, j) for i in range(n) for j in range(n) if img1[i][j] == 1)
        pos2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        for i1, j1 in pos1:
            for i2, j2 in pos2:
                overlaps[(i1 - i2, j1 - j2)] += 1
        return max(overlaps.values(), default=0)
            
