from ting_file_management.node import Node
import sys


class DoublyLinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 1 if value is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.head)

    def remove_from_head(self):
        node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = node.next
        return node.value

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def get_by_index(self, index):
        current = self.head
        if index >= self.length or not self.length or index < 0:
            return print("Posição inválida", file=sys.stderr)
        for _ in range(index):
            current = current.next
        return current
