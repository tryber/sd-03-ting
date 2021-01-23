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
        if index < 0 or index >= len(self.items):
            raise IndexError("Index fora do range")
        revArray = self.items[::-1]
        return revArray[index]
