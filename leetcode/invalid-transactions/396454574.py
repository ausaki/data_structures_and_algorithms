# title: invalid-transactions
# detail: https://leetcode.com/submissions/detail/396454574/
# datetime: Wed Sep 16 14:10:26 2020
# runtime: 168 ms
# memory: 14.3 MB

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
            result = set()
            m = collections.defaultdict(list)
            for tx in transactions:
                n, t, a, c = tx.split(',')
                t = int(t)
                a = int(a)
                if a > 1000:
                    result.add(tx)
                for tt, cc, tx_ in m[n]:
                    if c != cc and abs(t - tt) <= 60:
                        result.add(tx)
                        result.add(tx_)
                m[n].append([t, c, tx])
            return result