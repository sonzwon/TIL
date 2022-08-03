class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next



class Stack:
    def __init__(self, head=None):
        self.size = 0
        self.head = Node()
    
    def push(self, data):
        new_node = Node(data, self.head.get_next())
        self.head.set_next(new_node)
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            return None
        curr = self.head.get_next() #헤드의 넥스트는 항상 최신 노드이므로
        self.head.set_next(curr.get_next())
        curr.set_next(None)
        self.size -= 1
        return curr.get_data()
    
    def peak(self):
        if self.size == 0:
            return None
        return self.head.get_next().get_data()
    
    def size(self):
        return self.size