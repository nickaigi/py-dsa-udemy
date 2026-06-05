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
        O(n) linear time
        """
        if self.head is None:
            self.head = Node(value)
        else:
            curr = self.head

            while curr.next:
                curr = curr.next
            curr.next = Node(value)

    def prepend(self, value) -> None:
        """Add at the head of the list"""
        node = Node(value=value)
        node.next = self.head

    def insert(self, value, index: int) -> None:
        node = Node(value=value)
        if self.head is None:
            self.head = node

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
