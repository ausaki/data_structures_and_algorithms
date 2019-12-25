# title: exclusive-time-of-functions
# detail: https://leetcode.com/submissions/detail/287975666/
# datetime: Mon Dec 23 19:59:24 2019
# runtime: 76 ms
# memory: 12.7 MB

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        funcs = []
        start = -1
        for log in logs:
            fid, action, tp = log.split(':')
            fid = int(fid)
            tp = int(tp)
            if action == 'start':
                if funcs:
                    res[funcs[-1]] += tp - start         
                funcs.append(fid)
                start = tp
            else:
                funcs.pop()
                res[fid] += tp - start + 1
                start = tp + 1
        return res
        