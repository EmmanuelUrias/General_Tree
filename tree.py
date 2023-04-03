# Notes on General Tree. General Tree's unlike binary trees aren't limited to 2 children. The top node is called a Root node, middle nodes are just called Nodes, and the bottom nodes are called Leaf-nodes.
# The amount of levels is 0-indexed.
# The bottom nodes are known as children but everything on top of that is known as an ancestor

class TreeNode:
    def __init__(self, data):  # each element will be an instance of this class
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
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
        spaces = '  ' * self.get_level()
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()  # We're are using recursion to print the children of the children


def build_product_tree():
    root = TreeNode('Electronics')  # defining Root Node

    laptop = TreeNode('Laptop')  # Defining Node
    laptop.add_child(TreeNode('Mac'))  # Defining LeafNode
    laptop.add_child(TreeNode('Surface'))  # Defining LeafNode
    laptop.add_child(TreeNode('Thinkpad'))  # Defining LeafNode

    cellphone = TreeNode('Cell Phone')  # Defining Node
    cellphone.add_child((TreeNode('Iphone')))  # Defining LeafNode
    cellphone.add_child((TreeNode('Pixel')))  # Defining LeafNode
    cellphone.add_child((TreeNode('Vivo')))  # Defining LeafNode

    tv = TreeNode('TV')  # Defining Node
    tv.add_child(TreeNode('Samsung'))  # Defining LeafNode
    tv.add_child(TreeNode('LG'))  # Defining LeafNode

    root.add_child(laptop)  # Adding Node to Root children
    root.add_child(cellphone)  # Adding Node to Root children
    root.add_child(tv)  # Adding Node to Root children

    return root  # returning the built tree


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass
