# title: remove-comments
# detail: https://leetcode.com/submissions/detail/282690889/
# datetime: Sat Nov 30 23:07:22 2019
# runtime: 32 ms
# memory: 12.8 MB

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        block = False
        left = ''
        n = 0
        gonext = True
        while n < len(source):
            if gonext:
                line = source[n]
            else:
                gonext = True
            if block:
                i = line.find('*/')
                n += 1
                if i > -1:
                    if len(left) + len(line) - i - 2 > 0:
                        line = left + line[i+2:]
                        gonext = False
                        n -= 1
                    block = False
                    left = ''
                continue
            i = line.find('//')
            j = line.find('/*')
            if i == -1 and j == -1:
                res.append(line)
                n += 1
                continue
            if i == -1:
                i = 100
            if j == -1:
                j = 100
            if i < j:
                if i > 0:
                    res.append(line[:i])
                n += 1
                continue
            block = True
            left = line[:j]
            k = line.find('*/', j + 2)
            print(j, k)
            n += 1
            if k > j + 1:
                block = False
                left = ''
                if j + len(line) - k - 2 > 0:
                    line = line[:j] + line[k+2:]
                    print(line)
                    gonext = False
                    n -= 1
        return res        