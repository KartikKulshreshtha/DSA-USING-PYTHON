class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_node(self, child):
        child.parent = self
        self.children.append(child)
        
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
            
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else "->"
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
        
def Build_Node():
    root = TreeNode('Electronics')
    
    laptop = TreeNode('Laptop')
    laptop.add_node(TreeNode('HP'))
    laptop.add_node(TreeNode('DELL'))
    laptop.add_node(TreeNode('ASUS'))
    
    phones = TreeNode('Phones')
    phones.add_node(TreeNode('REALME'))
    phones.add_node(TreeNode('VIVO'))
    phones.add_node(TreeNode('REDMI'))
    
    watches = TreeNode('Watches')
    watches.add_node(TreeNode('SONATA'))
    watches.add_node(TreeNode('TITAN'))
    watches.add_node(TreeNode('REALME'))
    
    root.add_node(laptop)
    root.add_node(phones)
    root.add_node(watches)
    
    return root

if __name__ == '__main__':
    root = Build_Node()
    root.print_tree()