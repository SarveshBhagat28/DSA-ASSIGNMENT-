class Node:
    def __init__(self, book):
        self.book = book
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, book):
        new_node = Node(book)
        new_node.next = self.head
        self.head = new_node
        print(book, "added at beginning.")

    # Insert at end
    def insert_end(self, book):
        new_node = Node(book)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        print(book, "added at end.")

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty.")
            return

        print(self.head.book, "deleted from beginning.")
        self.head = self.head.next

    # Display
    def display(self):
        if self.head is None:
            print("Library catalog is empty.")
            return

        temp = self.head
        print("Library Catalog:")

        while temp is not None:
            print(temp.book)
            temp = temp.next


library = LinkedList()

while True:
    print("\n--- Library Catalog ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book title: ")
        library.insert_beginning(book)

    elif choice == "2":
        book = input("Enter book title: ")
        library.insert_end(book)

    elif choice == "3":
        library.delete_beginning()

    elif choice == "4":
        library.display()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
