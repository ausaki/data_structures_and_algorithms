# title: spiral-matrix
# detail: https://leetcode.com/submissions/detail/143648238/
# datetime: Tue Mar  6 09:50:21 2018
# runtime: 37 ms
# memory: N/A

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        m = len(matrix)
        if m == 0:
            return result
        
        n = len(matrix[0])
        if n == 0:
            return result
        
        px = 0
        py = 0
        x = 0
        y = 0
        prev_l = -1
        prev_t = 0
        prev_r = 0
        prev_b = 0
        while px < m and py < n:
            l, t, r, b = py, px, n - py - 1, m - px - 1
            if prev_l == -1:
                prev_l, prev_t, prev_r, prev_b = l, t, r, b
            elif not (l > prev_l and t > prev_t and r < prev_r and b < prev_b):
                break
            prev_l, prev_t, prev_r, prev_b = l, t, r, b
            
            if l > r or t > b:
                break
                
            for y in range(l, r + 1):
                print '1, y=', y
                result.append(matrix[t][y])
            
            if t == b:
                break
            for x in range(t + 1, b + 1):
                print '2, x=', x
                result.append(matrix[x][r])
            
            if r == l:
                break
            for y in range(r - 1, l - 1, -1):
                print '3, y=', y
                result.append(matrix[b][y])
                
            for x in range(b - 1, t, -1):
                print '4, x=', x
                result.append(matrix[x][l])
                
            px += 1
            py += 1
        
        return result
        
        