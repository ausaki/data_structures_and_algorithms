# title: reorder-data-in-log-files
# detail: https://leetcode.com/submissions/detail/403528294/
# datetime: Fri Oct  2 21:52:37 2020
# runtime: 36 ms
# memory: 14.3 MB

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def key(log):
            i = log.find(' ')
            if log[i + 1].isdigit():
                return (1, )
            else:
                return (0, log[i + 1:], log[:i])
        return sorted(logs, key=key)