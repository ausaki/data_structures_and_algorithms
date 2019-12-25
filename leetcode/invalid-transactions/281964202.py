# title: invalid-transactions
# detail: https://leetcode.com/submissions/detail/281964202/
# datetime: Wed Nov 27 11:26:39 2019
# runtime: 108 ms
# memory: 13.1 MB

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        N = len(transactions)
        d = {}
        result = set()
        for i in range(N):
            name, time, amount, city = transactions[i].split(',')
            time = int(time)
            amount = int(amount)
            if name not in d:
                d[name] = {}
            if city  not in d[name]:
                d[name][city] = []
            d[name][city].append([i, time])
            if amount > 1000:
                result.add(i)
            for ct, items in d[name].items():
                if ct != city:
                    for it in items:
                        if abs(it[1] - time) <= 60:
                            result.add(it[0])
                            result.add(i)
        return [transactions[i] for i in result]