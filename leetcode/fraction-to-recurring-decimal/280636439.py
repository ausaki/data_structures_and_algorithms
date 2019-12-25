# title: fraction-to-recurring-decimal
# detail: https://leetcode.com/submissions/detail/280636439/
# datetime: Fri Nov 22 00:45:12 2019
# runtime: 24 ms
# memory: 12.8 MB

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = ''
        if numerator == 0:
            return '0'
        if numerator ^ denominator < 0:
            result += '-'
        if numerator < 0:
            numerator = -numerator
        if denominator < 0:
            denominator = -denominator
        d, m = divmod(numerator, denominator)
        if m == 0:
            return result + str(d)
        result += str(d) + '.'
        cache = {}
        i = len(result) - 1
        numerator = m * 10
        while numerator > 0:
            if numerator in cache:
                j = cache[numerator]
                result = result[:j] + '(' + result[j:] + ')'
                break
            d, m = divmod(numerator, denominator)
            result += str(d)
            i += 1
            cache[numerator] = i
            numerator = m * 10
        return result
            
        