import graphviz

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
        
    def _insert(self, root, val):
        if root is None:
            node = TreeNode(val)
            node.height = 0
            return node
        if val < root.val:
            root.left = self._insert(root.left, val)
            root = self._rotate_left(root)
        else:
            root.right = self._insert(root.right, val)
            root = self._rotate_right(root)
        return root
    
    def find(self, val):
        node = self._find(val, self.root, None)
        return node

    def _find(self, val, root):
        if root is None:
            return None
        if val == root.val:
            return root
        if val < root.val:
            return self._find(val, root.left)
        return self._find(val, root.right)

    def _remove_max_right(self, root):
        if root.right:
            new_root, max_right = self._remove_max_right(root.right)
            root.right = new_root
            root = self._rotate_left(root)
            return root, max_right
        else:
            root.height = 0
            return root.left, root

    def _remove(self, val, root):
        if root is None:
            return None
        if val == root.val:
            if root.left:
                new_left, new_root = self._remove_max_right(root.left)
                new_root.left = new_left
                new_root.right = root.right
                root = self._rotate_right(new_root)
                return root
            else:
                root = root.right
            return root
        if val < root.val:
            root.left = self._remove(val, root.left)
            root = self._rotate_right(root)
            return root
        root.right = self._remove(val, root.right)
        root = self._rotate_left(root)
        return root

    def remove(self, val):
        self.root = self._remove(val, self.root)
    
    def _rotate_left(self, root):
        lh = self.height(root.left)
        rh = self.height(root.right)
        if lh - rh > 1:
            llh = self.height(root.left.left)
            if llh > rh:
                root = self.single_rotate_with_left(root)
            else:
                root = self.double_rotate_with_left(root)
        root.height = max(self.height(root.left), self.height(root.right)) + 1
        return root
    
    def _rotate_right(self, root):
        lh = self.height(root.left)
        rh = self.height(root.right)
        if rh - lh > 1:
            rlh = self.height(root.right.left)
            rrh = self.height(root.right.right)
            if rrh > lh:
                root = self.single_rotate_with_right(root)
            else:
                root = self.double_rotate_with_right(root)
        root.height = max(self.height(root.left), self.height(root.right)) + 1
        return root

    def single_rotate_with_left(self, k2):
        k1 = k2.left
        k2.left = k1.right
        k1.right = k2

        k2.height = max(self.height(k2.left), self.height(k2.right)) + 1
        k1.height = max(self.height(k1.left), self.height(k1.right)) + 1
        return k1

    def single_rotate_with_right(self, k2):
        k1 = k2.right
        k2.right = k1.left
        k1.left = k2

        k2.height = max(self.height(k2.left), self.height(k2.right)) + 1
        k1.height = max(self.height(k1.left), self.height(k1.right)) + 1
        return k1

    def double_rotate_with_left(self, k3):
        k3.left = self.single_rotate_with_right(k3.left)
        return self.single_rotate_with_left(k3)

    def double_rotate_with_right(self, k3):
        k3.right = self.single_rotate_with_left(k3.right)
        return self.single_rotate_with_right(k3)
    
    def height(self, node):
        return node.height if node else -1
    
    def display(self, filename='./avl_tree.dot'):
        def dis(node):
            if node is None:
                return
            name = label = str(node.val)
            graph.node(name, label)
            if node.left:
                l = dis(node.left)
                graph.edge(name, l)
            if node.right:
                r = dis(node.right)
                graph.edge(name, r)
            return name

        graph = graphviz.Digraph(name='avl_tree', format='png', node_attr={'fontcolor': 'black', 'shape': 'circle', 'fixedsize': 'True'})
        dis(self.root)
        graph.render(filename)

def main():
    tree = AVLTree()
    data = range(10)
    for i in data:
        tree.insert(i)
    tree.display()
    tree.remove(1)
    tree.display('./avl_tree.rm.dot')
    tree.remove(0)
    tree.display('./avl_tree.rm.1.dot')

main()