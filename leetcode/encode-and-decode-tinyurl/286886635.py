# title: encode-and-decode-tinyurl
# detail: https://leetcode.com/submissions/detail/286886635/
# datetime: Wed Dec 18 23:02:18 2019
# runtime: 36 ms
# memory: 12.7 MB

import random
class Codec:
    LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    SIZE = 6
    MAX_RANDOM = 100
    
    def __init__(self):
        self.mapping = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        size = self.SIZE
        while size <= len(self.LETTERS):
            i = 0
            while i < self.MAX_RANDOM:
                s = ''.join(random.choice(self.LETTERS) for i in range(size))
                if s not in self.mapping:
                    self.mapping[s] = longUrl
                    return s
            size += 1
        raise ValueError('no more url')
    

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.mapping.get(shortUrl, '')
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))