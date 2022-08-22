# [ Binary Search Tree ]
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def insert_node(self, node, value):
        if node is None:
            return Node(value)
        if value < node.data:
            node.left = self.insert_node(node.left, value)
        elif value > node.data:
            node.right = self.insert_node(node.right, value)
        return node


    def insert(self, value):
        self.root = self.insert_node(self.root, value)
        self._size += 1

    def contains(self, value):
        return self.contains_node(self.root, value)
    

    def contains_node(self, node, value):
        if node is None:
            return False  
        
        if value < node.data:
            return self.contains_node(node.left, value)
        elif value > node.data:
            return self.contains_node(node.right, value)
        else:  # value == node.data
            return True


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
            self._size -= 1
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.data = self.min_node(node.right)
            node.right = self.delete_node(node.right, node.data)
        return node

    def size(self):
        return self._size   

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
    
# [ Test Code ]
if __name__ == "__main__":
    btree = BinarySearchTree()
    for i in [3, 1, 2, 3, 8, 7]:
        print(f"btree.insert({i})")
        btree.insert(i)
        print(f"btree.size(): {btree.size()}")

    print("==================================")
    for i in [3, 1, 2, 3, 8, 7]:
        print(f"btree.contains({i}): {btree.contains(i)}")

    print("===================================")
    print(f"btree.preorder(): {btree.preorder()}")
    print(f"btree.inorder(): {btree.inorder()}")
    print(f"btree.postorder(): {btree.postorder()}")
    print("=====================================")

    print("btree.delete(2)")
    btree.delete(2)
    print("btree.delete(8)")
    btree.delete(8)
    print(f"btree.size(): {btree.size()}")

    print("==================================")
    for i in [3, 1, 2, 3, 8, 7]:
        print(f"btree.contains({i}): {btree.contains(i)}")

    print("===================================")
    print(f"btree.preorder(): {btree.preorder()}")
    print(f"btree.inorder(): {btree.inorder()}")
    print(f"btree.postorder(): {btree.postorder()}")
    print("=====================================")