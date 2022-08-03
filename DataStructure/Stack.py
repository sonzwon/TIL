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



# [[  백준 9012 : 괄호  ]]

# 내 코드 - 로직은 올바르게 돌아가지만 오답처리됨
N = int(input())
for _ in range(N):
    T = str(input())
    stack = []
    for t in T:
        if t == '(':
            stack.append(t)
        else:  
            if not stack:
                print("NO")
                break
            stack.pop()
    else:
        if len(stack)>0:
            print("NO")
        else:
            print("Yes")

# retry - 다른 사람 코드 참고
N = int(input())
for _ in range(N):
    stack = []
    T = input()
    VPS = True
    for t in T:
        if t == '(':
            stack.append('(')
        else:
            if not stack:
                VPS = False
            stack.pop
    if VPS and not stack:
        print('YES')
    elif not VPS or stack:
        print('NO')