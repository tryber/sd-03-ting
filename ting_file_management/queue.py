class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"Node({self.value}, {self.next})"

    def __str__(self):
        return f"{self.value}"

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
        current = self.head.next
        message = f"[{current}"
        while current is not self.tail:
            message += f", {current.value}"
            current = current.next

        return f"{message}]"

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


if __name__ == "__main__":
    flag = Queue()
    flag.enqueue(42)
    flag.enqueue(43)
    flag.enqueue(44)
    value = flag.search(0)
