# title: find-duplicate-file-in-system
# detail: https://leetcode.com/submissions/detail/287332267/
# datetime: Fri Dec 20 20:55:56 2019
# runtime: 88 ms
# memory: 22.5 MB

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for pathinfo in paths:
            parts = pathinfo.split(' ')
            dir = parts[0]
            for i in range(1, len(parts)):
                j = parts[i].find('(')
                filename = parts[i][:j]
                content = parts[i][j + 1:-1]
                groups[content].append(dir + '/' + filename)
        return [group for group in groups.values() if len(group) > 1]