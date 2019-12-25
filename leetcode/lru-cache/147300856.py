# title: lru-cache
# detail: https://leetcode.com/submissions/detail/147300856/
# datetime: Wed Mar 28 10:10:28 2018
# runtime: 656 ms
# memory: N/A

class LRUCache(object):
    """最久未使用缓存
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.keys = []
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self._update_lru_keys(key, True)
            return self.cache.get(key)
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache[key] = value
            self._update_lru_keys(key, True)
        else:
            if self.size == self.capacity:
                # cache is full, evicts lru key
                self._evict()
            self.cache[key] = value
            self._update_lru_keys(key, False)
            self.size += 1
    
    def _update_lru_keys(self, key, exists):
        if exists:
            self.keys.remove(key)
        self.keys.append(key)
    
    def _evict(self):
        lru_key = self.keys.pop(0)
        self.size -= 1
        self.cache.pop(lru_key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)