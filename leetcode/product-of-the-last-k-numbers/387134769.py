# title: product-of-the-last-k-numbers
# detail: https://leetcode.com/submissions/detail/387134769/
# datetime: Thu Aug 27 22:32:31 2020
# runtime: 292 ms
# memory: 29 MB

class ProductOfNumbers:

    def __init__(self):
        self.data = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.data.clear()
            self.data.append(1)
            return
        self.data.append(self.data[-1] * num)

    def getProduct(self, k: int) -> int:
        if k + 1 > len(self.data):
            return 0
        return self.data[-1] // self.data[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)