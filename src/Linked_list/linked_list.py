class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def insert_values(self, values):
        for value in values:
            self.insert_at_end(value)

    def insert_at(self, index, data):
        if not 0 <= index <= self.length():
            raise IndexError("Index out of range")

        if index == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = Node(data, current.next)

    def remove_at(self, index):
        if not 0 <= index < self.length():
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next

    def length(self):
        count = 0
        current = self.head
        # Use `while current`, not `while current.next`, or the last node is skipped
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        if self.head is None:
            return "Empty List"

        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " --> ".join(values)


if __name__ == "__main__":
    lst = LinkedList()

    for value in [9, 6, 7]:
        lst.insert_at_beginning(value)
    lst.insert_at_end(44)
    lst.insert_values(["Fares", "Faris", "Firas", "Feras"])

    print("Initial:      ", lst)
    print("Length:       ", lst.length())

    lst.remove_at(2)
    print("remove_at(2): ", lst)

    lst.insert_at(2, "BANANA")
    print("insert_at(2): ", lst)

    lst.insert_at(lst.length(), "END")
    print("insert at end:", lst)