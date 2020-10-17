# title: throne-inheritance
# detail: https://leetcode.com/submissions/detail/409458002/
# datetime: Fri Oct 16 21:49:10 2020
# runtime: 804 ms
# memory: 67.9 MB

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.g = collections.defaultdict(lambda: [1])
        self.king = kingName
        
    def birth(self, parentName: str, childName: str) -> None:
        self.g[parentName].append(childName)

    def death(self, name: str) -> None:
        self.g[name][0] = 0

    def getInheritanceOrder(self) -> List[str]:
        order = []
        g = self.g
        def dfs(name):
            children = g[name]
            if children[0] == 1:
                order.append(name)
            for i in range(1, len(children)):
                dfs(children[i])
        dfs(self.king)
        return order

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()