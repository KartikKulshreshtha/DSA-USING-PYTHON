class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        
    def insertion(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
    
    def deletion(self):
        temp = self.head
        self.head = temp.next
    
    def display(self):
        temp = self.head
        list = ''
        while temp is not None:
            list += str(f"{temp.data}->")
            temp = temp.next
        print(list)
    
    
if __name__ == '__main__':
    x = Queue()
    x.insertion(1)
    x.insertion(2)
    x.insertion(3)
    x.display()
    x.deletion()
    x.display()
    