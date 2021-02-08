from ting_file_management.doubly_linked_list import DoublyLinkedList
from collections.abc import Iterable
from ting_file_management.queue_iterator import QueueIterator


class Queue(Iterable):
    def __init__(self):
        self.__data = DoublyLinkedList()
        self.__length = 0

    def __iter__(self):
        return QueueIterator(self.__data)

    def __len__(self):
        return self.__length

    def __str__(self):
        return str(self.__data)

    def enqueue(self, value):
        self.__data.add_to_tail(value)
        self.__length += 1

    def dequeue(self):
        item = self.__data.remove_from_head()
        self.__length -= 1
        return item

    def search(self, index):
        if index >= self.__length or index < 0:
            raise IndexError
        node = self.__data.get_by_index(index)
        return node and node.value
    