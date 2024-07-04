class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def IsEmpty(self):
        return len(self.queue) == 0

    def IsFull(self):
        return len(self.queue) == self.max_size

    def Enqueue(self, item):
        if self.IsFull():
            print("Queue is full, cannot add element.")
        else:
            self.queue.append(item)
            print(f"Added {item} to the queue.")

    def Dequeue(self):
        if self.IsEmpty():
            print("Queue is empty, cannot remove element.")
        else:
            removed_item = self.queue.pop(0)
            print(f"Removed {removed_item} from the queue.")
            return removed_item

    def Show(self):
        if self.IsEmpty():
            print("Queue is empty.")
        else:
            print("Queue elements are:", self.queue)

def main():
    max_size = int(input("Enter the maximum size of the queue: "))
    queue = Queue(max_size)

    while True:
        print("\nMenu:")
        print("1. Check if the queue is empty")
        print("2. Check if the queue is full")
        print("3. Add element to the queue (Enqueue)")
        print("4. Remove element from the queue (Dequeue)")
        print("5. Show elements in the queue")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            if queue.IsEmpty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        elif choice == 2:
            if queue.IsFull():
                print("Queue is full.")
            else:
                print("Queue is not full.")
        elif choice == 3:
            item = input("Enter the character to add to the queue: ")
            queue.Enqueue(item)
        elif choice == 4:
            queue.Dequeue()
        elif choice == 5:
            queue.Show()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()