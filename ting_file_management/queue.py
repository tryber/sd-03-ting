# Implementa a fila na lista.
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'Node({self.value}, {self.next})'

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
        jsNode = Node(value, prev=self.tail.prev, next=self.tail)
        jsNode.prev.next = jsNode
        self.tail.prev = jsNode
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
        remove = self.head.next
        self.head.connect(remove.next)
        remove.reset()
        self.__length -= 1
        return remove.value


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
