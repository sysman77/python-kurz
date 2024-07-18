class UnfixedSizeStack:
  def __init__(self):
    self.items = []  # Use a list for dynamic size

  def is_empty(self):
    return len(self.items) == 0

  def is_full(self):
    # No need to check for full condition in unfixed size stack
    return False

  def push(self, data):
    self.items.append(data)
    print("Pushed:", data)

  def pop(self):
    if self.is_empty():
      print("Stack Underflow")
      return
    data = self.items.pop()
    print("Popped:", data)
    return data

  def peek(self):
    if self.is_empty():
      print("Stack is empty")
      return
    return self.items[-1]  # Access last element

  def size(self):
    return len(self.items)

  def clear(self):
    self.items = []
    print("Stack cleared")

def main():
  stack = UnfixedSizeStack()

  while True:
    print("\nMenu:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Is Empty?")
    print("6. Clear")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      data = int(input("Enter data to push: "))
      stack.push(data)
    elif choice == 2:
      stack.pop()
    elif choice == 3:
      print("Top element:", stack.peek())
    elif choice == 4:
      print("Stack size:", stack.size())
    elif choice == 5:
      print("Stack is empty:", stack.is_empty())
    elif choice == 6:
      stack.clear()
    elif choice == 7:
      break
    else:
      print("Invalid choice")

if __name__ == "__main__":
  main()
