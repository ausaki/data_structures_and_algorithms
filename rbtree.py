"""
红黑树的性质:

- 每一个节点要么是黑色, 要么是红色.

- 根节点是黑色的.

- 叶子节点是黑色的.

- 如果一个节点是红色的, 那么它的子节点必须是黑色的.

- 从一个节点到NULL节点的所有路径必须包含相同数量的黑色节点.
"""
import graphviz

RED = 'R'
BLACK = 'B'

DEBUG = False
_print = print
def print(*args):
    if DEBUG: _print(*args)


class RBNode:
    def __init__(self): 
        self.value: int = None
        self.color = RED
        self.left:RBNode = None
        self.right:RBNode = None
        self.parent:RBNode = None
    
    def get_parent(self) -> "RBNode":
        return self.parent
    
    def get_sibling(self) -> "RBNode":
        p = self.get_parent()
        if p is None:
            return
        return p.right if self == p.left else p.left

    def get_grandparent(self) -> "RBNode":
        p = self.get_parent()
        if p is None:
            return
        gp = p.get_parent()
        return gp

    def get_uncle(self) -> "RBNode":
        p = self.get_parent()
        uncle = p.get_sibling()
        return uncle

    def __str__(self):
        return f'{self.value}.{self.color}'



class RBTree:
    def __init__(self):
        self.root = None
    
    def find(self, value) -> RBNode:
        curr = self.root
        while curr and curr.value != value:
            curr = curr.left if value < curr.value else curr.right
        return curr

    def add(self, value:int):
        new_node = RBNode()
        new_node.value = value
        new_node.color = RED
        curr = self.root
        while curr:
            if new_node.value < curr.value:
                if curr.left is None:
                    curr.left = new_node
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = new_node
                    break
                curr = curr.right
        new_node.parent = curr
        self._insert(new_node)

    def _insert(self, node: RBNode) -> RBNode:
        print(f'insert node: {node.value}')
        parent = node.get_parent()
        # case 1
        if parent == None:
            print('insert case 1')
            node.color = BLACK
            self.root = node
            return
        
        # case 2
        if parent.color == BLACK:
            print('insert case 2')
            return
        
        uncle = node.get_uncle()
        grandparent = node.get_grandparent()
        
        # case 3
        if uncle and uncle.color == RED:
            print('insert case 3')
            parent.color = uncle.color = BLACK
            grandparent.color = RED
            return self._insert(grandparent)

        # case 4
        print('insert case 4')
        if parent == grandparent.left:
            if node == parent.right:
                self.rotateleft(parent)
                node, parent = parent, node
            self.rotateright(grandparent)
        else:
            if node == parent.left:
                self.rotateright(parent)
                node, parent = parent, node
            self.rotateleft(grandparent)
        
        parent.color = BLACK
        grandparent.color = RED
        
        if grandparent == self.root:
            print(f'grandparent {grandparent} is root and it\'s rotated, set parent `{parent}`to be new root')
            self.root = parent

    def remove(self, value):
        node = self.find(value)
        if node is None:
            print(f'remove: can\'t find value `{value}`')
            return
        m = self.getmax(node.left)
        if m :
            node.value = m.value
            node = m
        
        parent = node.get_parent()
        # simple case 1
        if node.color == RED:
            if node == parent.left:
                parent.left = None
            else:
                parent.right = None
            return

        # simple case 2
        child = node.left if node.left else node.right
        if node.color == BLACK and child:
            child.parent = parent
            child.color = BLACK
        else:
            self._remove(node)

        # node is maybe self.root
        if node == self.root:
            self.root = child
        else:
            if node == parent.left:
                parent.left = child
            else:
                parent.right = child

    def _remove(self, node: RBNode):

        # case 1
        if node.get_parent() is None:
            return
        
        # case 2
        sibling = node.get_sibling()
        parent = node.get_parent()
        if sibling.color == RED:
            parent.color = RED
            sibling.color = BLACK
            if node == parent.left:
                self.rotateleft(parent)
            else:
                self.rotateright(parent)
        
        # case3
        # because the case 2's rotation, node's sibling and parent is changed. 
        sibling = node.get_sibling()
        parent = node.get_parent()
        if (parent.color == BLACK and sibling.color == BLACK and 
            (sibling.left is None or sibling.left.color == BLACK) and 
            (sibling.right is None or sibling.right.color == BLACK)):
            
            sibling.color = RED
            self._remove(parent)
            return
        
        # case 4
        if parent.color == RED:
            sibling.color = RED
            parent.color = BLACK
            return

        # case5
        if (node == parent.left and sibling.left and sibling.left.color == RED and 
            (sibling.right is None or sibling.right.color == BLACK)):
            sibling.color = RED
            sibling.left.color = BLACK
            self.rotateright(sibling)
        elif (node == parent.right and sibling.right and sibling.right.color == RED and
                (sibling.left is None or sibling.left.color == BLACK)):
            sibling.color = RED
            sibling.right.color = BLACK
            self.rotateleft(sibling)
        
        # case6
        sibling = node.get_sibling()
        sibling.color = parent.color
        parent.color = BLACK
        if node == parent.left:
            sibling.right.color = BLACK
            self.rotateleft(parent)
        else:
            sibling.left.color = BLACK
            self.rotateright(parent)
        if parent == self.root:
            self.root = sibling

    def getmin(self, root):
        while root and root.left:
            root = root.left
        return root

    def getmax(self, root):
        while root and root.right:
            root = root.right
        return root
    
    @staticmethod
    def rotateleft(node:RBNode):
        child:RBNode = node.right
        if child is None:
            return
        node.right, child.left = child.left, node
        if node.right:
            node.right.parent = node
        if node.parent:
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        node.parent, child.parent = child, node.parent
    

    @staticmethod
    def rotateright(node):
        child = node.left
        if child is None:
            return
        node.left, child.right = child.right, node
        if node.left:
            node.left.parent = node
        if node.parent:
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        node.parent, child.parent = child, node.parent

    def display(self):
        queue = [self.root]
        while queue:
            l = len(queue)
            line = []
            for i in range(l):
                n = queue.pop(0)
                if n is None:
                    line.append(f'N.{BLACK}')
                else:
                    line.append(str(n))
                    queue.append(n.left)
                    queue.append(n.right)
            print(', '.join(line))
        print()
    
    def display2(self):
        def dis(node):
            if node is None:
                return
            name = label = str(node.value)
            color = 'black' if node.color == BLACK else 'red'
            graph.node(name, label, fillcolor=color, pencolor=color, bgcolor=color, color=color, style='filled')
            if node.left:
                l = dis(node.left)
                graph.edge(name, l)
            if node.right:
                r = dis(node.right)
                graph.edge(name, r)
            return name

        graph = graphviz.Digraph(name='rbtree', format='png', node_attr={'fontcolor': 'white', 'shape': 'circle', 'fixedsize': 'True'})
        dis(self.root)
        graph.render('./rbtree.dot')

if __name__ == '__main__':
    rbtree = RBTree()
    n = 20
    for i in range(1, n + 1):
        rbtree.add(i)
    rbtree.display2()

    rbtree.remove(3)
    rbtree.display()
    rbtree.remove(5)
    rbtree.display()
    rbtree.remove(8)
    rbtree.display()
    rbtree.remove(9)
    rbtree.display()