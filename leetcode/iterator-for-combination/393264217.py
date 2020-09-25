# title: iterator-for-combination
# detail: https://leetcode.com/submissions/detail/393264217/
# datetime: Wed Sep  9 20:52:20 2020
# runtime: 44 ms
# memory: 15.8 MB

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.it = itertools.combinations(characters, combinationLength)
        self.next_ = next(self.it)
        
    def next(self) -> str:
        s = ''.join(self.next_)
        self.next_ = next(self.it, None)
        return s
    
    def hasNext(self) -> bool:
        return self.next_ is not None
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()