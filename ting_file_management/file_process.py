class Queue:
    # Implementa a fila na lista.
    def __init__(self):
        self.tail = Node("TAIL", next=None, prev=self.head)
        self.head = Node("HEAD", prev=None)
        self.head.next = self.tail
        self.__length = 0

    def __str__(self):
        current = self.head.next
        message = f"[{current}"
        while current is not self.tail:
            message += f", {current.value}"
            current = current.next
        return f"{message}]"

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        node = Node(value, prev=self.tail.prev, next=self.tail)
        node.prev.next = node
        self.tail.prev = node
        self.__length += 1


    def search(self, index):
        if index >= self.__length or index < 0:
            raise IndexError
        current = self.head.next
        while current != self.tail and index > 0:
            current = current.next
            index -= 1
        return current.value


    def dequeue(self):
        if len(self) == 0:
            return None
        to_remove = self.head.next
        self.head.connect(to_remove.next)
        to_remove.reset()
        self.__length -= 1
        return to_remove.value


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"Node({self.data}, {self.next})"

    def __str__(self):
        return f"{self.data}"

    def reset(self):
        self.prev = None
        self.next = None

    def connect(self, other):
        self.next = other
        other.prev = self


if __name__ == "__main__":
    fila = Queue()
    fila.enqueue(42)
    fila.enqueue(43)
    fila.enqueue(44)
    valor = fila.search(0)
    print(fila, valor)
