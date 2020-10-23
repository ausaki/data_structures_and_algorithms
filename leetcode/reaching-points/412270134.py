# title: reaching-points
# detail: https://leetcode.com/submissions/detail/412270134/
# datetime: Fri Oct 23 22:36:48 2020
# runtime: 24 ms
# memory: 14 MB

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx == tx and sy == ty:
            return True
        if tx < sx or ty < sy:
            return False
        while tx > 1 and ty > 1:
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
        if tx == sx == 1 and ty >= sy:
            return True
        if ty == sy == 1 and tx >= sx:
            return True
        return False
        
        