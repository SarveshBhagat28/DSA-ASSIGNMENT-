class Queue:
    def __init__(self):
        self.f = -1
        self.r = -1
        self.QT = [0] * 5

    def insert(self, ticket):
        if self.r == 4:
            print("Queue is full")
            return

        self.r = self.r + 1
        self.QT[self.r] = ticket

        if self.f == -1:
            self.f = 0

        print(ticket, "added to the queue.")

    def delete(self):
        if self.f == -1:
            print("Queue is empty")
            return

        ticket = self.QT[self.f]
        print(ticket, "ticket processed.")

        if self.f == self.r:
            self.f = -1
            self.r = -1
        else:
            self.f = self.f + 1

    def display(self):
        if self.f == -1:
            print("Queue is empty")
            return

        print("Tickets in queue:")
        for i in range(self.f, self.r + 1):
            print(self.QT[i])


q = Queue()

while True:
    print("\n--- Ticket Booking Counter ---")
    print("1. Add Customer")
    print("2. Process Customer")
    print("3. Display Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        q.insert(name)

    elif choice == "2":
        q.delete()

    elif choice == "3":
        q.display()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
