class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.book, end=" ")
        inorder(root.right)


# Preorder Traversal
def preorder(root):
    if root:
        print(root.book, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.book, end=" ")


# Create Library Catalog Binary Tree
root = Node("Books")

root.left = Node("Fiction")
root.right = Node("Non-Fiction")

root.left.left = Node("Fantasy")
root.left.right = Node("Mystery")

root.right.left = Node("Science")
root.right.right = Node("History")


print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)
