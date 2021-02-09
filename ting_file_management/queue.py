class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"Node({self.value}, {self.next})"

    def reset(self):
        self.prev = None
        self.next = None

    def connect(self, other):
        self.next = other
        other.prev = self


class Queue:
    def __init__(self):
        self.head = Node("HEAD", prev=None)
        self.tail = Node("TAIL", next=None, prev=self.head)
        self.head.next = self.tail
        self.__length = 0

    def __len__(self):
        return self.__length

    def __str__(self):
        content = self.head.next
        message = f"[{content}"
        while content is not self.tail:
            message += f", {content.value}"
            content = content.next
        return f"{message}]"

    def enqueue(self, value):
        node = Node(value, prev=self.tail.prev, next=self.tail)
        node.prev.next = node
        self.tail.prev = node
        self.__length += 1

    def search(self, index):
        if index >= self.__length or index < 0:
            raise IndexError
        valueCurrent = self.head.next
        while valueCurrent != self.tail and index > 0:
            valueCurrent = valueCurrent.next
            index -= 1
        return valueCurrent.value

    def dequeue(self):
        if len(self) == 0:
            return None
        to_remove = self.head.next
        self.head.connect(to_remove.next)
        to_remove.reset()
        self.__length -= 1
        return to_remove.value


if __name__ == "__main__":
    fila = Queue()
    fila.enqueue(42)
    fila.enqueue(43)
    fila.enqueue(44)
    value = fila.search(0)
    print(fila.data)
    print(fila.search(0))
    print(fila.search(1))
    print(fila.search(2))
