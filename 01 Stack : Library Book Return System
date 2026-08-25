book_stack = []

while True:
    print("\n--- Library Book Return System ---")
    print("1. Return Book")
    print("2. Process Last Book")
    print("3. View Stack")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book title: ")
        book_stack.append(book)
        print(book, "added to stack.")

    elif choice == "2":
        if not book_stack:
            print("Stack is empty.")
        else:
            book = book_stack.pop()
            print(book, "processed for shelving.")

    elif choice == "3":
        if not book_stack:
            print("Stack is empty.")
        else:
            print("Books in stack (Top to Bottom):")
            for book in reversed(book_stack):
                print(book)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
