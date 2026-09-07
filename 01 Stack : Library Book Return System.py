class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return

        x = self.st[self.TOP]
        self.TOP -= 1
        return x


# Create Stack object
s = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = int(input("Enter value: "))
        s.push(x)

    elif choice == 2:
        x = s.pop()

        if x is not None:
            print("Popped element:", x)

    elif choice == 3:
        break

    else:
        print("Invalid choice")
       
