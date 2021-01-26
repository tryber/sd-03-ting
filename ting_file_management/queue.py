class Queue:
    # A fila será implementada sobre uma estrutura de lista.
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        # Insere no final da fi/lista
        return self.data.append(value)

    def dequeue(self):
        # Remove o primeiro elemento
        try:
            return self.data[0]
        except IndexError:
            return 'Índice inexistente'
        finally:
            del self.data[0]

    def search(self, index):
        if 0 <= index <= len(self.data):
            return self.data[index]
        raise IndexError


if __name__ == '__main__':
    fila = Queue()
    # fila.data = [1, 2, 3, 4, 5, 6]
    # print(fila.data)
    # fila.enqueue(7)
    # print(fila.data)
    # fila.enqueue(8)
    # print(fila.data)
    # fila.dequeue()
    # print(fila.data)
    fila.enqueue(42)
    fila.enqueue(43)
    fila.enqueue(44)
    print(fila.data)
    print(fila.search(0))
    print(fila.search(1))
    print(fila.search(2))
    # print(fila.search(5))
    print(fila.dequeue())
    print(fila.data)
    # print(fila.__len__())
