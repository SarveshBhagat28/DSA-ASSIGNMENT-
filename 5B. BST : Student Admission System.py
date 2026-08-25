class Node:
    def __init__(self, admission_no, name):
        self.admission_no = admission_no
        self.name = name
        self.left = None
        self.right = None


# Insert Student
def insert(root, admission_no, name):
    if root is None:
        return Node(admission_no, name)

    if admission_no < root.admission_no:
        root.left = insert(root.left, admission_no, name)
    else:
        root.right = insert(root.right, admission_no, name)

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
        print(current.admission_no, "-", current.name)
        current = current.right


# Non-Recursive Preorder
def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        current = stack.pop()
        print(current.admission_no, "-", current.name)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)


# Main Program
root = None

n = int(input("Enter number of students: "))

for i in range(n):
    admission_no = int(input("Enter admission number: "))
    name = input("Enter student name: ")

    root = insert(root, admission_no, name)


print("\n--- Inorder Student Records ---")
inorder(root)

print("\n--- Preorder Student Records ---")
preorder(root)
