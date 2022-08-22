class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert_node(self, node, value):
        if node is None:
            return Node(value)
        if val < node.data:
            node.left = self.insert_node(node.left, value)
        elif val > node.val:
            node.right = self.insert_node(node.right, value)
        return node

    def size(self):
        return self.size

    def insert(self, value):
        self.root = self.insert_node(self.root, value)
        self.size += 1

    def contains(self, value):
        return self.contains_node(self.root, value)
    

    def contains_node(self, node, value):
        if value < node.data:
            return self.contains_node(node.left, value)
        elif:
            return self.contains_node(node.right, value)
        else:  # value == node.data
            return True
        if node is None:
            return False  

    def delete(self, value):
        return self.delete_node(self.root, value)

    def delete_node(self, node, value):
        if node is None:
            return None

        if value < node.data:
            node.left = self.delete_node(node.left, value)
        elif value > node.data:
            node.right = self.delete_node(node.right, value)
        else:
            self.size -= 1
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.value = self.min_node(node.right)
            node.right = self.delete_node(node.right, node.value)
        return node

    def min_node(node):
        min_value = node.data
        while node.left is not None:
            min_value = node.left.data
            node = node.left
        return min_value
    
    def max_node(node):
        max_value = node.data
        while node.right is not None:
            max_value = node.right.data
            node = node.right
        return max_value

    def preorder(self):
        ret = []

        def visit(root):
            nonlocal ret
            if root is None:
                return ret
            ret.append(root.data)
            visit(root.left)
            visit(root.right)

        visit(self.root)
        return ret

    def inorder(self):
        ret = []

        def visit(root):
            nonlocal ret
            if root is None:
                return ret
            visit(root.left)
            ret.append(root.data)
            visit(root.right)

        visit(self.root)
        return ret

    def postorder(self):
        ret = []

        def visit(root):
            nonlocal ret
            if root is None:
                return ret
            visit(root.left)
            visit(root.right)
            ret.append(root.data)

        visit(self.root)
        return ret