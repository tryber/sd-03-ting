from ting_file_management.node import Node


class Queue:
    def __init__(self):
        self.head_value = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def is_empty(self):
        return not self.__length

    def insert_first(self, value):
        first_value = Node(value)
        first_value.next = self.head_value
        self.head_value = first_value
        self.__length += 1

    def enqueue(self, value):
        last_value = Node(value)
        current_value = self.head_value

        if self.is_empty():
            return self.insert_first(value)

        while current_value.next:
            current_value = current_value.next
        current_value.next = last_value
        self.__length += 1

    def dequeue(self):
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed.value

    def search(self, index):
        if index < 0 or index >= self.__length:
            raise IndexError('No such index')
        value_returned = None
        value_to_be_returned = self.head_value
        if value_to_be_returned:
            while index > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                index -= 1
            if value_to_be_returned:
                value_returned = Node(value_to_be_returned.value)
        return value_returned.value
