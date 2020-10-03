# title: powerful-integers
# detail: https://leetcode.com/submissions/detail/402286424/
# datetime: Tue Sep 29 23:24:23 2020
# runtime: 24 ms
# memory: 14.1 MB

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x == 1 and y == 1:
            return [2] if 2 <= bound else []
        if x == 1:
            x, y = y, x
        if y == 1:
            result = []
            a = 1
            while a < bound:
                result.append(a + 1)
                a *= x
            return result
        result = set()
        a = 1
        b = 1
        while a < bound:
            while b < bound:
                c = a + b
                if c <= bound:
                    result.add(c)
                else:
                    break
                b *= y
            a *= x
            b = 1
        return list(result)