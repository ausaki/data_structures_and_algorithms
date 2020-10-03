# title: equal-rational-numbers
# detail: https://leetcode.com/submissions/detail/402587072/
# datetime: Wed Sep 30 14:55:26 2020
# runtime: 32 ms
# memory: 14 MB

class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        def parse(s):
            m = re.match(r'(\d{1,4})(?:.(\d+)?(?:\((\d+)\))?)?', s)
            i, j, k = m.groups()
            if i is None:
                i = ''
            if j is None:
                j = ''
            if k is None:
                k = ''
            while j:
                l1 = len(j) - 1
                l2 = len(k) - 1
                while l1 >= 0 and l2 >= 0 and j[l1] == k[l2]:
                    l1 -= 1
                    l2 -= 1
                if l1 == len(j) - 1 and l2 == len(k) - 1:
                    break
                j, k = j[:l1 + 1], j[l1 + 1:] + k[:l2 + 1]
            if len(set(k)) == 1:
                k = k[0]
                if k == '0':
                    k = ''
            if len(k) == 4:
                if k[:2] == k[2:]:
                    k = k[:2]
            if not k and len(set(j)) == 1 and j[0] == '0':
                j = ''
            if k == '9':
                l = len(j)
                if l:
                    d = int(j) + 1
                    c, r = divmod(d, 10 ** l)
                    if c:
                        i = str(int(i) + 1) if i else '1'
                    j = str(r).rjust(l, '0')
                else:
                    i = str(int(i) + 1) if i else '1'
                k = ''
            return i, j, k
        i, j, k = parse(S)
        l, m, n = parse(T)
        return i == l and j == m and k == n
                