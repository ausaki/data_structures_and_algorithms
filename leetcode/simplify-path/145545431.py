# title: simplify-path
# detail: https://leetcode.com/submissions/detail/145545431/
# datetime: Sat Mar 17 18:04:09 2018
# runtime: 86 ms
# memory: N/A

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split('/')
        print paths
        real_path = [paths[0], ]
        for p in paths[1:]:
            if p == '..':
                if len(real_path) > 1:
                    real_path.pop()
            elif p == '.' or p == '':
                continue
            else:
                real_path.append(p)
        if len(real_path) == 1:
            real_path.append('')
        return '/'.join(real_path)
                
        