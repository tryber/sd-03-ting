from ting_file_management.__init__ import DoublyNode


class Queue:
    # initial commit
    def __init__(self):
        self.head = DoublyNode("HEAD")
        self.tail = DoublyNode("TAIL")
        self.head.next = self.tail
        self.tail.previous = self.head
        self.__length = 0

    def __len__(self):
        return self.__length

    def is_empty(self):
        return not self.__length

    def enqueue(self, value):
        node_value = DoublyNode(value)
        node_value.previous = self.tail.previous
        node_value.next = self.tail
        node_value.previous.next = node_value
        self.tail.previous = node_value
        self.__length += 1

    def dequeue(self):
        """Aqui irá sua implementação"""

    def search(self, index):
        """Aqui irá sua implementação"""
