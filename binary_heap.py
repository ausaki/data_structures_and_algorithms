class BinaryHeap:
    MAX_HEAP_SIZE = 100
    MIN_VALUE = -1

    def __init__(self, *args, **kwargs):
        self.heap = [None] * self.MAX_HEAP_SIZE
        self.heap[0] = self.MIN_VALUE
        self.last_index = 0


    def insert(self, value):
        self.last_index += 1
        index = self.last_index
        while self.heap[index // 2] >  value:
            self.heap[index] = self.heap[index // 2]
            index = index // 2
        self.heap[index] = value
    
    def getmin(self):
        min_value = self.heap[1]
        last_value = self.heap[self.last_index]
        self.last_index -= 1
        index = 1
        while 2 * index <= self.last_index:
            child = 2 * index
            if child < self.last_index and self.heap[child + 1] < self.heap[child]:
                child += 1
            if last_value > self.heap[child]: 
                self.heap[index] = self.heap[child]
                index = child
            else:
                break
        self.heap[index] = last_value
        return min_value

    def __str__(self):
        s = ''
        n = 1
        levels = []
        for i in range(1, self.last_index + 1):
            v = self.heap[i]
            s += '{} '.format(v)
            if i == n:
                n = (n << 1) + 1
                s += '\n'
        return s
                

def test():
    import random
    bh = BinaryHeap()
    for i in range(1, 10):
        bh.insert(random.randint(0, 100))
    print(bh)
    print('min:', bh.getmin())
    print(bh)

if __name__ == '__main__':
    test()
             
