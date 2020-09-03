# title: making-file-names-unique
# detail: https://leetcode.com/submissions/detail/380187159/
# datetime: Thu Aug 13 12:53:18 2020
# runtime: 444 ms
# memory: 34.6 MB

import re

class Solution:
    pattern = re.compile(r'\(\d+\)$')

    def getFolderNames(self, names: List[str]) -> List[str]:
        def add_to_folder(name):
            if not name: return
            if name[-1] != ')': return
            m = self.pattern.search(name)
            if not m: return
            l, r = m.span()
            i = int(name[l + 1:r - 1])
            if i == 0:
                return
            prefix_name = name[:l]
            if prefix_name not in folders:
                folders[prefix_name] = [-1, []]
            suffix = folders[prefix_name][1]
            bisect.insort(suffix, i)
            
        folders = {}
        result = []
        for name in names:
            if name not in folders:
                folders[name] = [0, []]
                result.append(name)
                add_to_folder(name)
            else:
                next = folders[name][0] + 1
                suffix = folders[name][1]
                while suffix and next >= suffix[0]:
                    suffix.pop(0)
                    next += 1
                folders[name][0] = next
                new_name = name
                if next == 0:
                    add_to_folder(name)
                else:
                    new_name = '{0}({1})'.format(name, next)
                    if new_name not in folders:
                        folders[new_name] = [0, []]
                    else:
                        folders[new_name][0] = 0
                result.append(new_name) 
        return result