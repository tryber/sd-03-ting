from ting_file_management.doubly_node import DoublyNode


class DoublyLinkedListIterator:
    def __init__(self, iterable):

        self.iterable = iterable

    def __next__(self):
        if self.iterable.next.next is None:
            raise StopIteration()

        self.iterable = self.iterable.next
        return self.iterable


class Queue:
    def __init__(self):
        self.head = DoublyNode("HEAD")
        self.tail = DoublyNode("TAIL")
        self.head.next = self.tail
        self.tail.previous = self.head
        self.__length = 0

    def __iter__(self):
        return DoublyLinkedListIterator(self.head)

    def __len__(self):
        return self.__length

    def __str__(self):
        return f"Queue(len={self.__length} value={self.head})"

    def enqueue(self, value):
        node_value = DoublyNode(value)
        node_value.previous = self.tail.previous
        node_value.next = self.tail
        self.tail.previous.next = node_value
        self.tail.previous = node_value
        self.__length += 1

    def dequeue(self):
        value_to_be_removed = self.head.next.value
        self.head.next = self.head.next.next
        self.head.next.previous = self.head
        self.__length -= 1
        return value_to_be_removed

    def search(self, index):
        if index < 0 or index >= self.__length:
            raise IndexError("Index fora do range")

        value_returned = None
        value_to_be_returned = self.head.next

        if value_to_be_returned:
            while index > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                index -= 1

            if value_to_be_returned:
                value_returned = value_to_be_returned.value

        return value_returned

    def is_empty(self):
        return not self.__length


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    # queue.enqueue(4)
    # queue.dequeue()
    # print(queue.search(0))
    # print(queue)
