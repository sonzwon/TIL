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
        
        
class LinkedQueue:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.size = 0
        
    def offer(self, data):
        new_node = Node(data)
        self.tail.set_next(new_node)
        self.tail = self.tail.get_next()
        self.size += 1
        
    def poll(self):
        if self.size == 0:
            raise Exception("Queue is Empty")
        curr = self.head.get_next()
        self.head.get_next() = curr.get_next()
        curr.set_next(None)
        self.size -= 1
        if self.head.get_next()==None:
            self.tail = self.head
        return curr.get_data()
    
    def peek(self):
        if self.size == 0:
            raise Exception("Queue is Empty")
        return self.head.get_next().get_data()
        
    def size(self):
        return self.size
    
    def clear(self):
        self.head.set_next(None)
        self.tail = self.head
        self.size = 0