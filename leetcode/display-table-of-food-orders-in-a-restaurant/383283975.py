# title: display-table-of-food-orders-in-a-restaurant
# detail: https://leetcode.com/submissions/detail/383283975/
# datetime: Thu Aug 20 00:44:50 2020
# runtime: 460 ms
# memory: 23.3 MB

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = collections.defaultdict(lambda : collections.defaultdict(int))
        foods = set()
        for _, t, f in orders:
            table[t][f] += 1
            foods.add(f)
        header = ['Table']
        header.extend(sorted(foods))
        result = [header]
        for t in sorted(map(int, table.keys())):
            row = [str(t)]
            foods = table[row[0]]
            for i in range(1, len(header)):
                f = header[i]
                row.append(str(foods[f]) if f in foods else '0')
            result.append(row)
        return result