class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.start=None
        self.itemcount=0
    
    def isempty(self):
        return self.start==0
    
    def push(self,data):
        n=node(data)
        n.next=self.start
        self.start=n
        self.itemcount+=1
        print(data,"has moved in stack")
    
    def pop(self):
        print(self.start.data,"has removed from stack")
        self.start=self.start.next
        self.itemcount-=1
        
    def peek(self):
        print(self.start.data,"is first element in stack")
        
    def size(self):
        print("the size is",self.itemcount)
s=stack()
s.push(10)
s.push(20)
s.pop()
s.peek()
s.size()