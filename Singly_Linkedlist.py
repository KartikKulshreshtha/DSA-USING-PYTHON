class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next=  next
class LinkedList:
    def __init__(self):
        self.head = None

    # This method is to insert the element at the begining of the linked list
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    # This method is to print all elements of the linked list
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        # print(itr)
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    # This method is to insert the element at the end of the LinkedList
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)


    # This method is to insert a list of elements into the linked list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.insert_at_begining(data)
            return
        if index == self.get_length()-1:
            self.insert_at_end(data)

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['K', 'A', 'R', 'T', 'I', 'K'])
    ll.get_length()
    ll.print()
    ll.insert_at(0, 'a')
    ll.print()
    