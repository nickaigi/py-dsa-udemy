"""LinkedList implementation"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def __repr__(self) -> str:
        return ""

    def __contains__(self) -> bool:
        return False

    def __len__(self) -> int:
        return 0

    def append(self, value) -> None:
        """
        Add at the end of the list
        O(n) - linear time
        """
        if self.head is None:
            self.head = Node(value)
        else:
            curr = self.head

            while curr.next:
                curr = curr.next
            curr.next = Node(value)

    def prepend(self, value) -> None:
        """
        O(1) - linear time
        Add at the head of the list
        """
        first_node = Node(value=value)
        first_node.next = self.head
        self.head = first_node

    def insert(self, value, index: int) -> None:
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node

    def delete(self, value) -> None:
        pass

    def pop(self, index: int) -> None:
        pass

    def get(self, index: int) -> None:
        pass

    def print(self):
        pass


if __name__ == "__main__":
    pass
