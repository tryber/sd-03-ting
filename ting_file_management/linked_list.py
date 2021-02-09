from .node import Node


class LinkedList:
    def __init__(self):
        self.head_value = None
        self._length = 0

    def __str__(self):
        return f"LinkedList(len={self._length}, value={self.head_value})"

    def __len__(self):
        return self._length

    def is_empty(self):
        return not self._length

    def insert_first(self, value):
        first_value = Node(value)
        first_value.next = self.head_value
        self.head_value = first_value
        self._length += 1

    def insert_last(self, value):
        if self.is_empty():
            return self.insert_first(value)

        new_last_value = Node(value)
        actual_last_value = self._get_node_at(len(self) - 1)
        actual_last_value.next = new_last_value
        self._length += 1

    def insert_at(self, value, position):
        if position < 1:
            return self.insert_first(value)
        if position >= len(self):
            return self.insert_last(value)
        current_value = self._get_node_at(position - 1)  # refactor
        # while position > 1:
        #     current_value = current_value.next
        #     position -= 1
        next_value = Node(value)
        next_value.next = current_value.next  #aqui pego a referencia mais atual e tranfiro para o novo item
        current_value.next = next_value  #aqui transfiro a referencia do antigo item mais novo para o atual
        self._length += 1

    def remove_first(self):
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next  #transforma o elemento cabeça no proximo da lista
            value_to_be_removed.next = None
            self._length -= 1
        return value_to_be_removed

    def remove_last(self):
        if len(self) <= 1:
            return self.remove_first()

        previous_to_be_removed = self._get_node_at(len(self) - 2)
        value_to_be_removed = previous_to_be_removed.next

        previous_to_be_removed.next = None
        self._length -= 1
        return value_to_be_removed

    def remove_at(self, position):
        if position < 1:
            return self.remove_first()
        if position >= len(self):
            return self.remove_last()

        previous_to_be_removed = self._get_node_at(position - 1)

        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = value_to_be_removed.next
        value_to_be_removed.next = None
        self._length -= 1

        return value_to_be_removed

    def get_element_at(self, position):
        value_returned = None
        value_to_be_returned = self._get_node_at(position)
        if value_to_be_returned:
            value_returned = Node(value_to_be_returned.value)
        return value_returned

    def clear(self):
        while not self.is_empty():
            self.remove_first()
        #optionally:
        # self.head_value = None
        # self._length = 0

    def _get_node_at(self, position):
        value_to_be_returned = self.head_value
        if self.head_value:
            while position > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
        return value_to_be_returned

    def index_of(self, value):
        position = 1
        current_value = self.head_value
        while current_value:
            if current_value.value == value:
                return position
            current_value = current_value.next
            position += 1
        return -1

    def make_set_of(self):
        new_set = set()
        current_value = self.head_value
        while current_value:
            new_set.add(current_value.value)
            current_value = current_value.next

        return new_set
