# title: making-file-names-unique
# detail: https://leetcode.com/submissions/detail/380195976/
# datetime: Thu Aug 13 13:16:51 2020
# runtime: 436 ms
# memory: 31.3 MB

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
                folders[prefix_name] = [-1]
            suffix = folders[prefix_name]
            heapq.heappush(suffix, i)
            
        folders = {}
        result = []
        for name in names:
            if name not in folders:
                folders[name] = [0]
                result.append(name)
                add_to_folder(name)
            else:
                suffix = folders[name]
                next = heapq.heappop(suffix) + 1
                while suffix and next >= suffix[0]:
                    heapq.heappop(suffix)
                    next += 1
                heapq.heappush(suffix, next)
                new_name = name
                if next == 0:
                    add_to_folder(name)
                else:
                    new_name = '{0}({1})'.format(name, next)
                    if new_name not in folders:
                        folders[new_name] = [0]
                    else:
                        heapq.heappush(folders[new_name], 0)
                result.append(new_name) 
        return result