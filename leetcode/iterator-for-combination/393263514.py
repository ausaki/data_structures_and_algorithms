# title: iterator-for-combination
# detail: https://leetcode.com/submissions/detail/393263514/
# datetime: Wed Sep  9 20:49:29 2020
# runtime: 40 ms
# memory: 15.8 MB

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.stop = characters[-combinationLength]
        self.it = itertools.combinations(characters, combinationLength)
        self.last = ''
        
    def next(self) -> str:
        s = ''.join(next(self.it))
        self.last = s[0]
        return s
    
    def hasNext(self) -> bool:
        return self.last != self.stop
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()