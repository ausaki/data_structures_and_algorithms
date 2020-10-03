'''
两种设置head和tail的思路

第一种：
head 和 tail 都指向当前对应的头和尾。问题是无法通过 head 和 tail 的位置来计算队列的长度。

length = (tail - head + 1) % size

1.
                head                tail
+----+----+----+----+----+----+----+----+----+----+----+
|    |    |    |  1 |  2 |  3 |  4 | 5  |    |    |    |
+----+----+----+----+----+----+----+----+----+----+----+
length = (7 - 3  + 1) % 11 = 5

2.
                tail                head
+----+----+----+----+----+----+----+----+----+----+----+
|  5 | 6  |  7 |  8 |    |    |    |  1 |  2 | 3  |  4 |
+----+----+----+----+----+----+----+----+----+----+----+
length = (3 - 7 + 1) % 11 = 8

3.
                               tail head
+----+----+----+----+----+----+----+----+----+----+----+
|  5 | 6  |  7 |  8 | 9  | 10 | 11 |  1 |  2 | 3  |  4 |
+----+----+----+----+----+----+----+----+----+----+----+
length = (6 - 7 + 1) % 11 = 0

4.
                                tail head
+----+----+----+----+----+----+----+----+----+----+----+
|    |    |    |    |    |    |    |    |    |    |    |
+----+----+----+----+----+----+----+----+----+----+----+
length = (6 - 7 + 1) % 11 = 0

上面 1 和 2 两种情况是通过公式计算出的长度是正确的。3 和 4两种情况则是混淆不清的，当队列长度等于0和等于总长度size时，公式计算结果都是0。
一种解决办法是使用一个变量保存队列的长度。


第二种：
head 指向当前头部的前一个位置（即下次往头部插入元素的位置），tail 指向当前尾部的后一个位置（即下次往尾部插入元素的位置）。另外，队列的长度初始化为比原来长度大 1。
这种方法解决了第一种方法的问题。

length = (tail - head - 1) % size

1.
            head                         tail
+----+----+----+----+----+----+----+----+----+----+----+----+
|    |    |    |  1 |  2 |  3 |  4 | 5  |    |    |    |    | (size = 11 + 1 = 12)
+----+----+----+----+----+----+----+----+----+----+----+----+
length = (8 - 2 - 1) % 12 = 5

2.
                     tail           head
+----+----+----+----+----+----+----+----+----+----+----+----+
|  5 | 6  |  7 |  8 |    |    |    |    |  1 |  2 | 3  |  4 |
+----+----+----+----+----+----+----+----+----+----+----+----+
length = (4 - 7 - 1) % 12 = 8

3.
                                  tail(head) 
+----+----+----+----+----+----+----+----+----+----+----+----+
|  5 | 6  |  7 |  8 | 9  | 10 | 11 |    |  1 |  2 | 3  |  4 |
+----+----+----+----+----+----+----+----+----+----+----+----+
length = (7 - 7 - 1) % 12 = 11

4.
                              head  tail
+----+----+----+----+----+----+----+----+----+----+----+----+
|    |    |    |    |    |    |    |    |    |    |    |    |
+----+----+----+----+----+----+----+----+----+----+----+----+
length = (7 - 6 - 1) % 12 = 0

'''
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k
        self.length = 0
        self.queue = [None] * self.size
        self.head = 0
        self.tail = 0
        
    def _reset(self):
        self.head = 0
        self.tail = 0
        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 1
            self.tail = 0
        self.head = (self.head - 1) % self.size
        self.queue[self.head] = value
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
            self.tail = -1
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        val = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        self.length -= 1
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        val = self.queue[self.tail]
        self.tail = (self.tail - 1) % self.size
        self.length -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.length == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.length == self.size


# Your MyCircularDeque object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyCircularDeque(10)
    param_1 = obj.insertFront(1)
    param_2 = obj.insertLast(2)
    param_2 = obj.insertLast(3)
    param_2 = obj.insertLast(4)
    param_3 = obj.deleteFront()
    param_4 = obj.deleteLast()
    param_5 = obj.getFront()
    param_6 = obj.getRear()
    param_7 = obj.isEmpty()
    param_8 = obj.isFull()