# title: integer-to-roman
# detail: https://leetcode.com/submissions/detail/115907888/
# datetime: Mon Aug 28 15:31:20 2017
# runtime: 212 ms
# memory: N/A

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mapper = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }
        subs = [1, 10, 100]
        roman = [1, 5, 10, 50, 100, 500, 1000]
        range_ = zip(roman, roman[1:] + [4000])
        for i, (l, r) in enumerate(range_):
            if num >= l and num < r:
                if l in subs:
                    if r - l <= num:
                        return mapper[l] + mapper[r] + self.intToRoman(num - (r - l))
                else:                       
                    a = roman[i - 1]
                    if a in subs and r - a <= num:
                        return mapper[a] + mapper[r] + self.intToRoman(num - (r - a))
                return mapper[l] + self.intToRoman(num - l)
        return ''
                        
            