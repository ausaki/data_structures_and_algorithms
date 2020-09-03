# title: circle-and-rectangle-overlapping
# detail: https://leetcode.com/submissions/detail/384240292/
# datetime: Fri Aug 21 23:44:39 2020
# runtime: 20 ms
# memory: 13.9 MB

class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        t, b, l, r = y_center + radius, y_center - radius, x_center - radius, x_center + radius
        print(t, b, l, r)
        if y1 > t or y2 < b or x2 < l or x1 > r:
            return False
        if y1 <= b and y2 >= t and x2 >= r and x1 <= l:
            print('true 0')
            return True
        dis = (x_center - (x1 + x2) / 2) ** 2 + (y_center - (y1 + y2) / 2) ** 2
        if dis <= radius ** 2:
            print('true 00')
            return True
        if l <= x1 <= r:
            diff = math.sqrt(radius ** 2 - (x_center - x1) ** 2)
            Y1 = y_center + diff
            Y2 = y_center - diff
            if y1 <= Y1 <= y2 or y1 <= Y2 <= y2:
                print('true 1')
                return True
        if l <= x2 <= r:
            diff = math.sqrt(radius ** 2 - (x_center - x2) ** 2)
            Y1 = y_center + diff
            Y2 = y_center - diff
            if y1 <= Y1 <= y2 or y1 <= Y2 <= y2:
                print('true 2')
                return True
        if b <= y1 <= t:
            diff = math.sqrt(radius ** 2 - (y_center - y1) ** 2)
            X1 = x_center + diff
            X2 = x_center - diff
            if x1 <= X1 <= x2 or x1 <= X2 <= x2:
                print('true 3')
                return True
        if b <= y2 <= t:
            diff = math.sqrt(radius ** 2 - (y_center - y2) ** 2)
            X1 = x_center + diff
            X2 = x_center - diff
            if x1 <= X1 <= x2 or x1 <= X2 <= x2:
                print('true 4')
                return True
        return False
        