# title: largest-time-for-given-digits
# detail: https://leetcode.com/submissions/detail/403090331/
# datetime: Thu Oct  1 20:28:46 2020
# runtime: 32 ms
# memory: 14.1 MB

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        a = sorted(itertools.permutations(arr))
        b = (2, 3, 5, 9)
        while a and (a[-1] > b or a[-1][2] >= 6):
            a.pop()
        return '{}{}:{}{}'.format(*a[-1]) if a else ''