# title: apply-discount-every-n-orders
# detail: https://leetcode.com/submissions/detail/387054595/
# datetime: Thu Aug 27 17:19:41 2020
# runtime: 772 ms
# memory: 21.3 MB

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = (100 - discount) / 100
        self.products = dict(zip(products, prices))
        self.cnt = 0
        
    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cnt += 1
        val = sum(self.products[p] * a for p, a in zip(product, amount))
        if self.cnt == self.n:
            self.cnt = 0
            return val * self.discount
        return val


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)