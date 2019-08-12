class Entry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def find(self, key):
        index = self._hash(key)
        head = self.table[index]
        entry = head
        while entry is not None and entry.key != key:
            entry = entry.next
        if entry is not None:
            return entry.value
        return None
    
    def insert(self, key, value):
        index = self._hash(key)
        head = self.table[index]
        entry = head
        while entry is not None and entry.key != key:
            entry = entry.next
        if entry is None:
            new_entry = Entry(key, value)
            new_entry.next = head
            self.table[index] = new_entry
        else:
            entry.value = value
    
    def delete(self, key):
        index = self._hash(key)
        head = self.table[index]
        entry = head
        prev = None
        while entry is not None and entry.key != key:
            prev = entry
            entry = entry.next
        if entry is None:
            raise Exception(f'{key} not exist')
        if entry is head:
            self.table[index] = entry.next
        else:
            prev.next = entry.next
        return entry.value

    def _hash(self, key):
        # return hash(key)
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            h = 0
            for c in key:
                h = (h << 5) + c
            return h % self.size
        return hash(key) % self.size
    
    def __str__(self):
        s = ''
        for i, entry in enumerate(self.table):
            s += '{} -> '.format(i)
            while entry is not None:
                s += '[{k}: {v}] -> '.format(k=entry.key, v=entry.value)
                entry = entry.next
            s += 'None\n'
        return s


if __name__ == '__main__':
    import random

    h = HashTable()
    for i in range(10):
        k = random.randint(1, 100)
        h.insert(k, int(random.random() * 10))
    print(h)