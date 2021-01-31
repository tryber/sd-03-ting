from ting_file_management.doubly_node import DoublyNode

# implementando a fila como uma lista duplamente ligada

# as implementações dos metodos são baseadas no material da Trybe


class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.head = DoublyNode("HEAD")
        self.tail = DoublyNode("TAIL")
        self.head.next = self.tail
        self.tail.previous = self.head
        self.__length = 0

    def __len__(self):
        """Aqui irá sua implementação"""
        return self.__length

    def is_empty(self):
        return not self.__length

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        # Ordem FIFO, inserindo ao final da doubled list
        node_value = DoublyNode(value)
        node_value.next = self.tail
        node_value.previous = self.tail.previous
        node_value.previous.next = node_value
        self.tail.previous = node_value
        self.__length += 1

    def dequeue(self):
        """Aqui irá sua implementação"""
        # Ordem FIFO, removendo ao inicio da doubled list
        value_to_be_removed = None
        if not self.is_empty():
            value_to_be_removed = self.head.next
            element_later_than_removed = value_to_be_removed.next
            self.head.next = element_later_than_removed
            element_later_than_removed.previous = self.head
            value_to_be_removed.reset()
            self.__length -= 1
        return value_to_be_removed.value

    def __get_node_at(self, position):
        value_to_be_returned = None
        if self.head.next != self.tail:
            value_to_be_returned = self.head.next
            while position > 0:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
        return value_to_be_returned

    def search(self, index):
        """Aqui irá sua implementação"""
        value_returned = None
        if index > self.__length - 1 or index < 0:
            raise IndexError
        value_to_be_returned = self.__get_node_at(index)
        if value_to_be_returned:
            value_returned = DoublyNode(value_to_be_returned.value)
        return value_returned.value
