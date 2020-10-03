# title: largest-time-for-given-digits
# detail: https://leetcode.com/submissions/detail/403091846/
# datetime: Thu Oct  1 20:36:06 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        a = sorted(itertools.permutations(arr))
        calc = lambda x: (x[0] * 10 + x[1]) * 60 + x[2] * 10 + x[3]
        b = calc([2, 3, 5, 9])
        while a and (calc(a[-1]) > b or a[-1][2] >= 6):
            a.pop()
        return '{}{}:{}{}'.format(*a[-1]) if a else ''