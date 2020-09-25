# title: brace-expansion-ii
# detail: https://leetcode.com/submissions/detail/397523442/
# datetime: Sat Sep 19 00:42:36 2020
# runtime: 36 ms
# memory: 14.2 MB

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        exp = '{' + expression + '}'
        n = len(exp)
        
        def union(sets):
            res = set()
            for s in sets:
                res |= s
            return res
        
        def product(sets):
            s1 = sets[0]
            for i in range(1, len(sets)):
                s = set()
                s2 = sets[i]
                for a in s1:
                    for b in s2:
                        s.add(a + b)
                s1 = s
            return s1
        
        def parse(i):
            j = i
            while j < n and exp[j].islower():
                j += 1
            if j > i:
                return {exp[i:j], }, j
            if exp[i] == '{':
                i += 1
                op = ''
                or_set = []
                pro_set = []
                while True:
                    s1, i = parse(i)
                    if exp[i] == '}':
                        i += 1
                        if pro_set:
                            pro_set.append(s1)
                        else:
                            or_set.append(s1)
                        break
                    if exp[i] == ',':
                        i += 1
                        if pro_set:
                            pro_set.append(s1)
                            s1 = product(pro_set)
                            pro_set.clear()
                        or_set.append(s1)
                    else:
                        pro_set.append(s1)
                if pro_set:
                    or_set.append(product(pro_set))
                return union(or_set), i
        
        return sorted(parse(0)[0])