class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


# Create Library Catalog
def create_tree():
    book = input("Enter category (-1 for no category): ")

    if book == "-1":
        return None

    root = Node(book)

    print("Left category of", book)
    root.left = create_tree()

    print("Right category of", book)
    root.right = create_tree()

    return root


# Inorder: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.book, end=" ")
        inorder(root.right)


# Preorder: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.book, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.book, end=" ")


# Main Program
print("===== LIBRARY BOOK CATALOG =====")

root = create_tree()

print("\n----- Inorder Traversal -----")
inorder(root)

print("\n----- Preorder Traversal -----")
preorder(root)

print("\n----- Postorder Traversal -----")
postorder(root)
