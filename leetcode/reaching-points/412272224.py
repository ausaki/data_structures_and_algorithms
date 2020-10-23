# title: reaching-points
# detail: https://leetcode.com/submissions/detail/412272224/
# datetime: Fri Oct 23 22:45:10 2020
# runtime: 20 ms
# memory: 14 MB

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx == tx and sy == ty:
            return True
        while tx >= sx and ty >= sy:
            if tx > ty:
                tx = tx % ty
                if sy == ty and sx % sy == tx:
                    return True
            elif tx < ty:
                ty = ty % tx
                if sx == tx and sy % sx == ty:
                    return True
            else:
                return False 
        return False
        
        