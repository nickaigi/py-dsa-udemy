"""Implement a stack"""


class Stack:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self) -> int:
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(f"stack.isEmpty() -> {stack.isEmpty()}")
    print(f"stack.push(1) -> {stack.push(1)}")
    print(f"stack.push('two') -> {stack.push('two')}")
    print(f"stack.peek() ->{stack.peek()}")
