class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        if len(self.second) > 0:
            return self.second[len(self.second) -1]
        else:
            while len(self.first) > 1:
                self.second.append(self.first.pop())
            front = self.first.pop()
            self.second.append(front)
            return front
        
        
    def pop(self):
        if len(self.second) > 0:
            return self.second.pop()
        else:
            while len(self.first) > 1:
                self.second.append(self.first.pop())
            return self.first.pop()
        
        
        
    def put(self, value):
        self.first.append(value)
        

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
