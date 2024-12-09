class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the list.

        :param data: The data to be added to the end of the list.
        """

        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        """Display the linked list."""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def rotate_right(self, k):
        """Rotate the list to the right by k places.

        :param k: The number of places to rotate the list.
        """
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0:
            return
        steps_to_new_head = length - k
        new_tail = self.head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        new_head.prev = None
        tail.next = self.head
        self.head.prev = tail
        self.head = new_head


def main():
    dll = DoublyLinkedList()
    for val in [1, 2, 3, 4, 5]:
        dll.append(val)
    print("Original list:")
    dll.display()
    dll.rotate_right(2)
    print("Rotated list by k=2:")
    dll.display()
    dll = DoublyLinkedList()
    for val in [0, 1, 2]:
        dll.append(val)
    print("\nOriginal list:")
    dll.display()
    dll.rotate_right(4)
    print("Rotated list by k=4:")
    dll.display()


if __name__ == '__main__':
    main()
