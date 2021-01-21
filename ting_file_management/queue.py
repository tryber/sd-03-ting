from double_node import DoublyNode


class Queue:
    def __init__(self):
        self.head = DoublyNode("HEAD")
        self.tail = DoublyNode("TAIL")
        self.head.next = self.tail
        self.tail.previous = self.head
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        """Aqui irá sua implementação"""

    def dequeue(self):
        """Aqui irá sua implementação"""

    def search(self, index):
        """Aqui irá sua implementação"""
