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

    def __contains__(self, value) -> bool:
        """
        O(n) linear Time
        """
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    def __len__(self) -> int:
        """
        O(n) linear time
        """
        last = self.head
        count = 0
        while last is not None:
            count += 1
            last = last.next
        return count

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
        O(1) - constant time
        Add at the head of the list
        """
        first_node = Node(value=value)
        first_node.next = self.head
        self.head = first_node

    def insert(self, value, index: int) -> None:
        """
        O(1) - linear time
        """
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
        temp = self.head

        if temp is not None and temp.value == value:
            self.head = temp.next
            temp = None  # optional, free the reference
            return

        prev = None
        while temp is not None and temp.value != value:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        prev.next = temp.next
        temp = None  # optional, free the reference

    def pop(self, index: int) -> None:
        pass

    def get(self, index: int) -> None:
        pass

    def print(self):
        pass


if __name__ == "__main__":
    pass
