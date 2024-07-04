class PriorityQueue:
  def __init__(self):
    self.items = []

  def IsEmpty(self):
    return len(self.items) == 0

  def IsFull(self):
    return False  # Priority queue is never considered full

  def InsertWithPriority(self, char, priority):
    item = (priority, char)
    self.items.append(item)
    self.items.sort(reverse=True)  # Sort by priority (highest first)

  def PullHighestPriorityElement(self):
    if self.IsEmpty():
      return None
    priority, char = self.items.pop()
    return char

  def Peek(self):
    if self.IsEmpty():
      return None
    priority, char = self.items[0]
    return char

  def Show(self):
    if self.IsEmpty():
      print("Queue is Empty")
    else:
      print("Queue Elements (Priority, Character):")
      for priority, char in self.items:
        print(f"({priority}, {char})")

def main():
  queue = PriorityQueue()

  while True:
    print("\nMenu:")
    print("1. Insert with Priority")
    print("2. Pull Highest Priority Element")
    print("3. Peek")
    print("4. Show")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      char = input("Enter a character: ")
      priority = int(input("Enter its priority: "))
      queue.InsertWithPriority(char, priority)
    elif choice == 2:
      char = queue.PullHighestPriorityElement()
      if char:
        print("Dequeued character with highest priority:", char)
    elif choice == 3:
      char = queue.Peek()
      if char:
        print("Character with highest priority (not removed):", char)
      else:
        print("Queue is Empty")
    elif choice == 4:
      queue.Show()
    elif choice == 5:
      print("Exiting...")
      break
    else:
      print("Invalid choice!")

if __name__ == "__main__":
  main()
