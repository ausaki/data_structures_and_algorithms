ENTRY_EMPTY = 0
ENTRY_DUMMY = 1
ENTRY_NORMAL = 2

def get_status(s):
    m = {
        ENTRY_EMPTY: 'ENTRY_EMPTY',
        ENTRY_DUMMY: 'ENTRY_DUMMY',
        ENTRY_NORMAL: 'ENTRY_NORMAL'
    }
    return m.get(s)

class Entry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.status = ENTRY_EMPTY


class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = []
        for i in range(self.size):
            self.table.append(Entry(None, None))
    
    def _find(self, key):
        index = self._hash(key)
        i = 1
        print('index: ', end='')
        while self.table[index].status != ENTRY_EMPTY and self.table[index].key != key:
            print(index, end=' ')
            index += 2 * i - 1
            index %= self.size 
            i += 1
        print(index)
        return index     

    def find(self, key):
        index = self._find(key)
        entry = self.table[index] 
        if entry.status == ENTRY_NORMAL:
            return entry.value
        return None
    
    def insert(self, key, value):
        index = self._find(key)
        entry = self.table[index]
        entry.key = key
        entry.status = ENTRY_NORMAL
        entry.value = value

    
    def delete(self, key):
        index = self._find(key)
        entry = self.table[index]
        if entry.status == ENTRY_EMPTY or entry.status == ENTRY_DUMMY:
            raise Exception('{} not exists'.format(key))
        entry.status = ENTRY_DUMMY
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
            s += '{i} -> [{k}: {v}] {s}\n'.format(i=i, k=entry.key, v=entry.value, s=get_status(entry.status))
        return s

class HashTable2(HashTable):
    def _find(self, key):
        index = self._hash(key)
        i = 1
        while self.table[index].status != ENTRY_EMPTY:
            entry = self.table[index]
            if entry.status == ENTRY_NORMAL and entry.key == key:
                break
            index += 2 * i - 1
            i += 1
        return index
    
    def insert(self, key, value):
        index = self._hash(key)
        i = 1
        first_dummy = None 
        entry = self.table[index]
        while entry.status != ENTRY_EMPTY:
            if first_dummy is None and entry.status == ENTRY_DUMMY:
                first_dummy = entry
            if entry.status == ENTRY_NORMAL and entry.key == key:
                break
            index += 2 * i - 1
            i += 1
            entry = self.table[index]
        if entry.status == ENTRY_EMPTY and first_dummy is not None:
            entry = first_dummy
        entry.key = key
        entry.value = value
        entry.status = ENTRY_NORMAL


if __name__ == '__main__':
    import random

    h = HashTable2(10)
    # for i in range(5):
    #     k = random.randint(1, 100)
    #     v = int(random.random() * 10)
    #     print('insert {} {}'.format(k, v))
    #     h.insert(k, v)
    #     print(h)

    h.insert(1, 2)
    h.insert(11, 3)
    h.delete(1)
    print(h)
    h.insert(11, 5)
    print(h)
    h.insert(1, 10)
    print(h)