# title: latest-time-by-replacing-hidden-digits
# detail: https://leetcode.com/submissions/detail/446966828/
# datetime: Sun Jan 24 10:40:10 2021
# runtime: 40 ms
# memory: 14.1 MB

class Solution:
    def maximumTime(self, time: str) -> str:
        res = []
        if time[0] == '?':
            if time[1] == '?':
                res.append('2')
                res.append('3')
            elif time[1] in '0123':
                res.append('2')
                res.append(time[1])
            else:
                res.append('1')
                res.append(time[1])
        else:
            res.append(time[0])
            if time[1] == '?':
                if time[0] in '01':
                    res.append('9')
                else:
                    res.append('3')
            else:
                res.append(time[1])
        if time[3] == '?':
            if time[4] == '?':
                res.append('5')
                res.append('9')
            else:
                res.append('5')
                res.append(time[4])
        else:
            res.append(time[3])
            if time[4] == '?':
                res.append('9')
            else:
                res.append(time[4])
        return '{}{}:{}{}'.format(*res)