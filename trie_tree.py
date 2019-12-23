class TrieTree:
    END = '#'

    def __init__(self):
        self.root = {}
    
    def add(self, s):
        node = self.root
        for c in s:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[self.END] = self.END
    
    def search(self, s):
        node = self.root
        for c in s:
            if c not in node:
                return False
            node = node[c]
        return self.END in node

    def prefix(self, s):
        prefix = ''
        node = self.root
        for c in s:
            if self.END in node:
                return prefix
            if c not in node:
                return ''
            prefix += c
            node = node[c]
        if self.END in node:
            return prefix
        return ''


if __name__ == '__main__':
    trie = TrieTree()
    trie.add('hello')
    trie.add('world')
    trie.add('hi')
    print('search hello', trie.search('hello'))
    print('prefix hi', trie.prefix('hfa'))