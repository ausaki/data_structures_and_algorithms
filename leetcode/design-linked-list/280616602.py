# title: design-linked-list
# detail: https://leetcode.com/submissions/detail/280616602/
# datetime: Thu Nov 21 22:34:57 2019
# runtime: 148 ms
# memory: 13.7 MB

class Node:
    
    def __init__(self):
        self.val = None
        self.next = None
        self.prev = None
        
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.holder = Node()
        self.holder.next = self.holder.prev = self.holder
        
        self._length = 0
    
    def _get(self, index: int) -> Node:
        if index < 0 or index >= self._length:
            return None
        if index < self._length - index:
            node = self.holder.next
            while index > 0:
                node = node.next
                index -= 1
            return node
        else:
            node = self.holder.prev
            index = self._length - index
            while index > 1:
                node = node.prev
                index -= 1
            return node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._get(index)
        return node.val if node is not None else -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new = Node()
        new.val = val
        new.next = self.holder.next
        new.prev = self.holder
        self.holder.next = new
        new.next.prev = new
        
        self._length += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new = Node()
        new.val = val
        new.next = self.holder
        new.prev = self.holder.prev
        self.holder.prev = new
        new.prev.next = new
        
        self._length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self._length:
            self.addAtTail(val)
            return
        node = self._get(index)
        if node is None:
            return
        new = Node()
        new.val = val
        new.next = node
        new.prev = node.prev
        node.prev = new
        new.prev.next = new
        
        self._length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self._get(index)
        if node is None:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None
        
        self._length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)