class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.items = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.items)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        return self.items.insert(0, value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.items.pop()

    def search(self, index):
        result = []
        try:
            result.append(self.items[index + len(self.items) - 1])
        except IndexError:
            index
        except ValueError:
            index
        return result
