# title: minimum-genetic-mutation
# detail: https://leetcode.com/submissions/detail/285854870/
# datetime: Sat Dec 14 16:44:38 2019
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
        
        start = encode(start)
        end = encode(end)
        new_bank = set()
        for i, gene in enumerate(bank):
            new_bank.add(encode(gene))
        bank = new_bank
        queue = collections.deque()
        queue.append(start)
        level = 0
        while queue:
            for i in range(len(queue)):
                gene = queue.popleft()
                for i in range(8):
                    for j in range(4):
                        g = (gene & ~(3 << (i * 2))) | (j << (i * 2))
                        if g in bank:
                            if g == end:
                                return level + 1
                            queue.append(g)
                            bank.remove(g)
            level += 1
        return -1