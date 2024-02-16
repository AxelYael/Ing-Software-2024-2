"""  
Ejercicio 1: Contar valles
"""
def count_valleys(steps):
    level = 0
    valleys = 0
    for step in steps:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        elif step == 'D':
            level -= 1
    return valleys


"""  
Ejercicio 2: Árbol binario de búsqueda
"""
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while current:
                parent = current
                if key <= current.key:
                    current = current.left
                else:
                    current = current.right
            if key <= parent.key:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent

    def pre_order_traversal(self, node):
        if node:
            print(node.key, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.key, end=" ")
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.key, end=" ")


# Ejemplo de uso:
steps = ['U', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'D']
print("Número de valles:", count_valleys(steps))

tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Pre-order traversal:")
tree.pre_order_traversal(tree.root)
print("\nIn-order traversal:")
tree.in_order_traversal(tree.root)
print("\nPost-order traversal:")
tree.post_order_traversal(tree.root)
