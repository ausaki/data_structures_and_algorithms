# title: lru-cache
# detail: https://leetcode.com/submissions/detail/147339447/
# datetime: Wed Mar 28 14:07:48 2018
# runtime: 267 ms
# memory: N/A

"""
该算法思路来源于：https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/lru_cache/lru_cache.ipynb
"""
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LinkedList(object):
    """
    double linked list
    * notice boundary conditions
    """
    def __init__(self):
        self.head = None
        self.tail = None
    
    def _empty(self):
        return self.head is None and self.tail is None
    
    def __str__(self):
        if self._empty():
            return 'None'
        h = self.head
        s = []
        while h:
            s.append(str(h.val))
            h = h.next
        return 'LinkedList(' + '<->'.join(s) + ')'
    
    def move_to_front(self, node):
        if self._empty():
            return False
        if node == self.head:
            # if node is head, then no need to move it.
            return True
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        self.append_to_front(node)
        return True
    
    def append_to_front(self, node):
        if self._empty():
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
        return True
    
    def remove_from_tail(self):
        if self.head == self.tail:
            self.head = self.tail = None
            return True
        else:
            if self.head and self.tail:
                node = self.tail.prev
                node.next = None
                self.tail = node
                return True
            else:
                return False
            

class LRUCache(object):
    """最久未使用缓存
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.linkedlist = LinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key)
        if node is None:
            return -1
        val = node.val
        self.linkedlist.move_to_front(node)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.linkedlist.move_to_front(node)
            return
        
        if self.size == self.capacity:
            self.cache.pop(self.linkedlist.tail.key)
            self.linkedlist.remove_from_tail()
            self.size -= 1
        node = Node(key, value)
        self.linkedlist.append_to_front(node)
        self.cache[key] = node
        self.size += 1