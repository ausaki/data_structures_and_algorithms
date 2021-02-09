import hashlib

def create_hashfunc(i, size):
    def h(x):
        salt = i.to_bytes(1, 'big', signed=False)
        if isinstance(x, int):
            x = x.to_bytes(8, 'big', signed=False)
        y = hashlib.md5(salt + x).digest()
        return int.from_bytes(y, byteorder='big', signed=False)
    
    return h

class BloomFilter:
    def __init__(self, size=1<<15, nhashs=5) -> None:
        self.size = size
        self._bitmap = bytearray(size // 8)
        self.hashs = [create_hashfunc(i, size) for i in range(nhashs)]
    
    def add(self, item):
        for h in self.hashs:
            i = h(item) % self.size
            i, j = divmod(i, 8)
            self._bitmap[i] |= 1 << j

    def hasitem(self, item):
        for h in self.hashs:
            i = h(item) % self.size
            i, j = divmod(i, 8)
            if not self._bitmap[i] & (1 << j):
                return False
        return True

    def __contains__(self, item):
        return self.hasitem(item)



def main():
    import random
    bf = BloomFilter()
    s = set()
    for i in range(1000):
        x = random.randint(1, 10000)
        s.add(x)
        bf.add(x)
    for x in s:
        if x not in bf:
            print('False negtive')
    for x in range(20000, 20000 + 100):
        if x in bf:
            print('False positive')

    bf.add(20000)
    print(20000 in bf)
    
if __name__ == '__main__':
    main()