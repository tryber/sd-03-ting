class Queue:
    # A fila será implementada sobre uma estrutura de lista.
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        # Método append insere no final da lista, logo não serve
        return self.data.insert(0, value)

    def dequeue(self):
        # Sem parâmetro, este método remove o último ítem
        return self.data.pop()

    def search(self, index):
        try:
            return self.data[index]
        except IndexError:
            return 'Índice inválido'


if __name__ == '__main__':
    fila = Queue()
    fila.data = [1, 2, 3, 4, 5, 6]
    print(fila.data)
    fila.enqueue(7)
    print(fila.data)
    fila.enqueue(8)
    print(fila.data)
    fila.dequeue()
    print(fila.data)
    print(fila.search(2))
    print(fila.search(15))
    print(fila.__len__())
