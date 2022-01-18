class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    
    def print(self):
        if self.head is None:
            print("Your Linked List is Empty!!")
            return
        itr = self.head
        # print(itr)
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
        
    def get_length(self):
        count = 0
        n = self.head
        while n:
            count += 1
            n = n.next
        return count
            
    def insert_into_empty_list(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            print("Your Linked List is Empty!!")
            
    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            node = Node(data)
            n.next = node
            node.prev = n
            
    def delete_at_start(self):
        if self.head is None:
            print("Your list is empty!!")
            return
        else:
            self.head = self.head.next
            
    def delete_at_end(self):
        if self.head is None:
            print("Your list is empty!!")
            return
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.prev.next = None
            
    def delete_node_at_given_position(self, position):
        if position < 0 or position > self.get_length():
            raise Exception('Invalid Index!!!')
        if position == 0:
            self.delete_at_start()
            return
        if position == self.get_length()-1:
            self.delete_at_end()
            return
        itr = self.head
        count = 0
        while itr:
            if count == position-1:
                itr.next = itr.next.next
                itr.next.prev = itr
                break
            itr = itr.next
            count += 1
        
                
                
    def insert_at_given_position(self, data, position):
        if position < 0 or position > self.get_length():
            raise Exception('Invalid Index!!!')
        if position == 0:
            self.insert_at_begining(data)
            return
        if position == self.get_length()-1:
            self.insert_at_end(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == position-1:
                node = Node(data)
                node.next = itr.next
                node.prev = itr
                itr.next = node
                itr.next.prev = node
            itr = itr.next
            count +=1
                
if __name__ == '__main__':
    x = DoublyLinkedList()
    x.insert_at_end(1)
    x.insert_at_end(2)
    x.insert_at_end(3)
    x.insert_at_end(5)
    x.print()
    x.insert_at_given_position(0, 2)
    x.print()
    