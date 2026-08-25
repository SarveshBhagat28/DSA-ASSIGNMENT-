class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


# Non-Recursive Inorder
def inorder(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")
        current = current.right


# Non-Recursive Preorder
def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        current = stack.pop()
        print(current.data, end=" ")

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)


# Main Program
root = None

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter value: "))
    root = insert(root, value)

print("\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)
