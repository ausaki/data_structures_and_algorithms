# title: making-file-names-unique
# detail: https://leetcode.com/submissions/detail/380253354/
# datetime: Thu Aug 13 15:53:06 2020
# runtime: 388 ms
# memory: 27.5 MB

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
                folders[prefix_name] = 0
            
        folders = {}
        result = []
        for name in names:
            if name not in folders:
                folders[name] = 1
                result.append(name)
                # add_to_folder(name)
            else:
                suffix = folders[name]
                new_name = name
                if suffix > 0:
                    new_name = '{}({})'.format(name, suffix)
                while new_name in folders:
                    suffix += 1
                    new_name = '{}({})'.format(name, suffix)
                folders[name] = suffix + 1
                folders[new_name] = 0
                # else:
                #     heapq.heappush(folders[new_name], 0)
                result.append(new_name) 
        return result