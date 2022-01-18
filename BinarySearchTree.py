from platform import node


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add the data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
                
        else:
            # add the data in the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
                
    def in_order_traversal(self):
        elements = []
         
        #  visiting the left subtree
        if self.left:
            elements += self.left.in_order_traversal()
        
        # visiting the base node
        elements.append(self.data)
        
        #  visiting the right subtree
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
    
    def pre_order_traversal(self):
        elements = []
        
        # visiting the base node first
        elements.append(self.data)
    
        # visiting the left node
        if self.left:
            elements += self.left.pre_order_traversal()
        
        # visiting the right node
        if self.right:
            elements += self.right.pre_order_traversal()
            
        return elements
        
        
    def post_order_traversal(self):
        elements = []
    
        # visiting the left node
        if self.left:
            elements += self.left.pre_order_traversal()
        
        # visiting the right node
        if self.right:
            elements += self.right.pre_order_traversal()
            
        # visiting the base node first
        elements.append(self.data)
        
        return elements
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def total_sum(self):
        leftsum = self.left.total_sum() if self.left else 0
        rightsum = self.right.total_sum() if self.right else 0
        return self.data + leftsum + rightsum
    
    def search(self, val):
        
        # if the data is equal to the current data
        if self.data == val:
            return True
        
        if val < self.data:
            # means the val is in the left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            # means the val is in the right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root



if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    number_tree = build_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.pre_order_traversal())
    print(number_tree.post_order_traversal())
    print(number_tree.search(20))
    print(number_tree.find_max())
    print(number_tree.find_min())
    print(number_tree.total_sum())