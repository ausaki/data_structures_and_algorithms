# title: minimum-genetic-mutation
# detail: https://leetcode.com/submissions/detail/285837161/
# datetime: Sat Dec 14 14:43:46 2019
# runtime: 24 ms
# memory: 12.8 MB

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        '''
        A   C   G   T
        00  01  10  11
        '''
        def encode(gene):
            m = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
            code = 0
            for i, c in enumerate(gene):
                code |= m[c] << (2 * (7 - i))
            return code
        
        def decode(gene):
            m = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
            res = ''
            for i in range(7, -1, -1):
                res += m[gene >> (2 * i) & 3]
            return res
        
        def mutate(gene, seen):
            # print(decode(gene))
            if gene == end:
                return len(seen)
            seen.add(gene)
            res = 10
            for i in range(8):
                for j in range(4):
                    g = (gene & ~(3 << (i * 2))) | (j << (i * 2))
                    if g in bank and g not in seen:
                        res = min(res, mutate(g, seen))
            seen.remove(gene)
            return res
        
        start = encode(start)
        # print(decode(start))
        end = encode(end)
        new_bank = set()
        for i, gene in enumerate(bank):
            new_bank.add(encode(gene))
        bank = new_bank
        res = mutate(start, set())
        return res if res <= 8 else -1