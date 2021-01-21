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
        node_value = DoublyNode(value)
        node_value.previous = self.tail.previous
        node_value.next = self.tail
        node_value.previous.next = node_value
        self.tail.previous = node_value
        self.__length += 1

    def dequeue(self):
        value_to_be_removed = None
        if not self.is_empty():
            value_to_be_removed = self.head.next
            element_later_than_removed = value_to_be_removed.next
            self.head.next = element_later_than_removed
            element_later_than_removed.previous = self.head
            value_to_be_removed.reset()
            self.__length -= 1
        return value_to_be_removed

    def search(self, index):
        value_returned = None
        if index > self.__length - 1:
            raise Exception("Index out of range")
        value_to_be_returned = self.__get_node_at(index)
        if value_to_be_returned:
            value_returned = DoublyNode(value_to_be_returned.value)
        return value_returned
