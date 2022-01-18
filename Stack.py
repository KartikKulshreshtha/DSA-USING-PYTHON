class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.Stacksize = 0
        
    def push(self, data):
        temp = Node(data)
        if self.top is None:
            self.top = temp
            self.Stacksize = self.Stacksize + 1
        else:
            temp.next = self.top
            self.top = temp
            self.Stacksize = self.Stacksize + 1
    
    def pop(self):
        try:
            if self.top is None:
                raise Exception('Stack is empty!!')
            else:
                temp = self.top
                self.top = self.top.next
                tempData = temp.data
                self.Stacksize = self.Stacksize - 1
                del temp
                return tempData
            
        except Exception as e:
            print(str(e))
                
    def isEmpty(self):
        if self.top is None:
            print("True")
            return
        else:
            print("False")
            return
        
        
    def size(self):
        print(self.Stacksize)
        return
    
    
    def display(self):
        temp = self.top
        if self.top is None:
            print("Your stack is empty!!")
            return
        else:
            while temp is not None:
                print(f"{temp.data}->", end=" ")
                temp = temp.next
            return      
if __name__ == '__main__':
    x = Stack()
    x.push(1)
    x.push(2)
    x.push(3)
    x.push(4)
    x.push(5)
    x.pop()
    x.isEmpty()
    x.size()
    x.display()
    